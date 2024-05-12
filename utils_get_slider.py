import cv2

from utils_global import imread_grayscale

SLIDER = imread_grayscale("pics/slider_02.jpg")

def get_slider_pos(img, slider=SLIDER):
    img_edges = cv2.Canny(img, 50, 150)
    slider_edges = cv2.Canny(slider, 50, 150)

    result = cv2.matchTemplate(img_edges, slider_edges, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val > 0.15:
        top_left = max_loc
        return (int(top_left[0] + slider.shape[1] / 2), int(top_left[1] + slider.shape[0] / 2))

    return (None, None)