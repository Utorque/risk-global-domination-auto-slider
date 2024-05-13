from PIL import ImageGrab
import cv2
import numpy as np
from time import sleep
import pyautogui

from utils_detect_attack_mode import is_attack_mode
from utils_get_win_chance import get_win_chance, setup_pytesseract
from utils_get_slider import get_slider_pos
from utils_global import imread_grayscale

PYTESSERACT_PATH = r'D:\Applications\Tesseract-OCR\tesseract.exe'

DRAG_DURATION = 0.15
DRAG_DISTANCE = 50
ATTACK_MODE_SLEEP = 0.02

SLIDER = imread_grayscale("pics/slider_03.jpg")

def get_grayscale_screenshot(sc_width, sc_height):
    screen = np.array(ImageGrab.grab(bbox=(0,0,sc_width,sc_height)))
    return cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)

def move_slider(position, direction, distance = DRAG_DISTANCE):
    pyautogui.moveTo(position, duration=0)

    if direction == 'left':
        new_position = (position[0] - distance, position[1])
    elif direction == 'right':
        new_position = (position[0] + distance, position[1])
    else:
        return
    
    pyautogui.dragTo(new_position, duration=DRAG_DURATION, button='left')


if __name__ == "__main__":
    screen_width = 1920
    screen_height = 1080

    setup_pytesseract(PYTESSERACT_PATH)

    done = False

    while True:
        sleep(0.3)
        gray_screen = get_grayscale_screenshot(screen_width, screen_height)

        if not is_attack_mode(gray_screen):
            done = False

        while is_attack_mode(gray_screen) and not done:
            win_chance = get_win_chance(gray_screen)
            slider_pos = get_slider_pos(gray_screen, SLIDER)
            
            print(win_chance)
            print(slider_pos)
            
            while win_chance >= 100: # moving left while 100%
                move_slider(slider_pos, "left")
                sleep(ATTACK_MODE_SLEEP)
                gray_screen = get_grayscale_screenshot(screen_width, screen_height)
                slider_pos = get_slider_pos(gray_screen, SLIDER)
                win_chance = get_win_chance(gray_screen)
                if win_chance is None: break
            if win_chance is None: continue
            
            while win_chance < 100: # moving back to the right
                slider_pos = (min(screen_width, slider_pos[0] + 5), slider_pos[1])
                move_slider(slider_pos, "right")
                sleep(ATTACK_MODE_SLEEP)
                gray_screen = get_grayscale_screenshot(screen_width, screen_height)
                slider_pos = get_slider_pos(gray_screen, SLIDER)
                win_chance = get_win_chance(gray_screen)
            
            done = True

