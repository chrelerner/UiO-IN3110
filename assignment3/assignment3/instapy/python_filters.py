"""pure Python implementation of image filters"""

import numpy as np
from PIL import Image


def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)
    # iterate through the pixels, and apply the grayscale transform
    
    for i in range( len(image) ):
        row = image[i]
        for j in range( len(row) ):
            pixel = row[j]
            
            red, green, blue = pixel[0], pixel[1], pixel[2]
            weighted_sum = (red * 0.21) + (green * 0.72) + (blue * 0.07)
            gray_image[i][j] = weighted_sum
            
    gray_image = gray_image.astype("uint8")
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

if __name__ == "__main__":
    
    im = Image.open("leaf.jpg")
    resized = im.resize((im.width // 2, im.height // 2))
    leaf_data = np.asarray(resized)
    leaf_grayscale_data = python_color2gray(leaf_data)
    leaf_grayscale = Image.fromarray(leaf_grayscale_data)
    leaf_grayscale.save("leaf_grayscale.jpg")
    
    
    im = Image.open("rain_hand.jpg")
    resized = im.resize((im.width // 2, im.height // 2))
    rain_hand_data = np.asarray(resized)
    rain_hand_grayscale_data = python_color2gray(rain_hand_data)
    rain_hand_grayscale = Image.fromarray(rain_hand_grayscale_data)
    rain_hand_grayscale.save("rain_hand_grayscale.jpg")
    
    
    
