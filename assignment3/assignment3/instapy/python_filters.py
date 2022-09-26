"""pure Python implementation of image filters"""

import numpy as np


def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)
    # iterate through the pixels, and apply the grayscale transform

    for row in image:
        for pixel in row:
            
            red, green, blue = pixel[0], pixel[1], pixel[2]
            weighted_sum = (red * 0.21) + (green * 0.72) + (blue * 0.07)
            gray_image[row][pixel] = weighted_sum
            
    gray_image = gray_image.astype("uint8")
    gray_image = gray_image.reshape(gray_image.shape[0], gray_image.shape[1])
    
    return gray_image


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)
    # Iterate through the pixels
    # applying the sepia matrix

    ...

    # Return image
    # don't forget to make sure it's the right type!
    return sepia_image
