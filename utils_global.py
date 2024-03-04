import cv2
import numpy as np

def imread_grayscale(image_path) -> cv2.typing.MatLike:
    """
    Returns the grayscale matlike of a path
    """
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

def gradient_convolution(image_mat, kernel = None) -> cv2.typing.MatLike:
    """Gives the gradient of a picture"""
    
    kernel = np.array([[ -1, -2, -1],
                       [ -2,  12, -2],
                       [ -1, -2, -1]], dtype=np.float32) if kernel is None else kernel
    
    img_convolved = cv2.filter2D(image_mat, -1, kernel)
    
    return img_convolved

def show_image(image_mat) -> None:
    """
    Display an image from a matrix-like object.

    Parameters:
    - image_mat: An image represented as a matrix-like object (numpy ndarray).
    """
    # Create a window to display the image
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    
    # Display the image
    cv2.imshow('Image', image_mat)
    
    # Wait for a key press and then destroy all OpenCV windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def display_circles(image_mat, circles):
    """
    Display the image with detected circles drawn on it.

    Parameters:
    - image_mat: The original image as a matrix-like object (numpy ndarray).
    - circles: A list of tuples, where each tuple contains the (x, y) center coordinates and radius of a circle.
    """
    # Copy the image to avoid modifying the original
    image_with_circles = image_mat.copy()
    for x, y, r in circles:
        # Draw the outer circle
        cv2.circle(image_with_circles, (x, y), r, (0, 255, 0), 2)
        # Draw the center of the circle
        cv2.circle(image_with_circles, (x, y), 2, (0, 0, 255), 3)
    
    # Use the previously defined function to show the image
    show_image(image_with_circles)
