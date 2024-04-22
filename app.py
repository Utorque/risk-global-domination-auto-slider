from PIL import ImageGrab
import cv2
import numpy as np
from time import sleep

from utils_detect_attack_mode import is_attack_mode
from utils_get_win_chance import get_win_chance, setup_pytesseract


def get_grayscale_screenshot(sc_width, sc_height):
    screen = np.array(ImageGrab.grab(bbox=(0,0,sc_width,sc_height)))
    return cv2.cvtColor(screen,cv2.COLOR_RGB2GRAY)

if __name__ == "__main__":
    screen_width = 1920
    screen_height = 1080

    setup_pytesseract()

    while True:
        sleep(1)
        gray_screen = get_grayscale_screenshot(screen_width, screen_height)
        while is_attack_mode(gray_screen):
            print(get_win_chance(gray_screen))
            sleep(0.2)
            gray_screen = get_grayscale_screenshot(screen_width, screen_height)

    