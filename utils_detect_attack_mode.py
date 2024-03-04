import cv2
import numpy as np

def is_attack_mode(img_mat) -> bool:
    """
    Main function to decide whether the game is in attack mode or not
    """
    circles = find_circles(img_mat)
    return check_circle_positions(img_mat,circles)

def find_circles(gray_image_mat : cv2.typing.MatLike, blur_size=15):
    """
    Detect circles in an image using the Hough Circle Transform.

    Parameters:
    - image_mat: An image represented as a matrix-like object (numpy ndarray).

    Returns:
    - List of tuples, where each tuple contains the (x, y) center coordinates and radius of a circle.
    """

    # Apply blur to reduce noise
    gray_blurred = cv2.medianBlur(gray_image_mat, blur_size)

    # Detect circles
    circles = cv2.HoughCircles(
        gray_blurred, 
        cv2.HOUGH_GRADIENT, 
        dp=1, 
        minDist=200, 
        param1=50, 
        param2=30, 
        minRadius=int(len(gray_image_mat[0])/10), 
        maxRadius=int(len(gray_image_mat[0])/9)
        )
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        return [(x, y, r) for x, y, r in circles[0, :]]
    else:
        return []

def check_circle_positions(image_mat, circles):
    """
    Check if there are exactly two circles, with one in the top-left and the other in the top-right quadrant.

    Parameters:
    - image_mat: The original image as a matrix-like object (numpy ndarray).
    - circles: A list of tuples, where each tuple contains the (x, y) center coordinates and radius of a circle.

    Returns:
    - True if the conditions are met, False otherwise.
    """
    # Check if there are exactly two circles
    if len(circles) != 2:
        return False

    # Calculate the midpoints to divide the image into quadrants
    height, width = image_mat.shape[:2]
    mid_x, mid_y = width / 2, height / 2

    # Initialize flags for circle positions
    top_left_found = False
    top_right_found = False

    for x, y, _ in circles:
        if x < mid_x and y < mid_y:
            top_left_found = True
        elif x > mid_x and y < mid_y:
            top_right_found = True

    # Return True if one circle is in the top-left and the other in the top-right quadrant
    return top_left_found and top_right_found