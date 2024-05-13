import pytesseract
import cv2


def setup_pytesseract(tesseract_ocr_path = r'D:\Applications\Tesseract-OCR\tesseract.exe'):
    pytesseract.pytesseract.tesseract_cmd = tesseract_ocr_path

def _get_win_chance_pic(img : cv2.typing.MatLike):
    """
    Returns the part of a game image where the win chance is
    """
    h, w = img.shape
    top_y = int(h * 0.07)
    bottom_y = int(h * 0.125)
    left_x = int(w * 0.45) 
    right_x = int(w * 0.55) 
    return img[top_y:bottom_y, left_x:right_x]

def get_win_chance(gray_screen: cv2.typing.MatLike) -> int:
    try:
        crop = _get_win_chance_pic(gray_screen)
        text : str = pytesseract.image_to_string(crop, config='--psm 6')
        return int("".join([char for char in text if char.isdigit()]))
    except Exception as e:
        print(e)
        return None