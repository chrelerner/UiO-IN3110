"""numba-optimized filters"""
from numba import jit
import numpy as np
from PIL import Image

@jit
def numba_color2gray(image: np.array) -> np.array:
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


def numba_color2sepia(image: np.array) -> np.array:
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
    
    im = Image.open("../test/leaf.jpg")
    #resized = im.resize((im.width // 2, im.height // 2))
    #data = np.asarray(resized)
    data = np.asarray(im)
    print("Before convertion.\n")
    filtered_data = numba_color2gray(data)
    print("After conversion.\n")
    filtered_im = Image.fromarray(filtered_data)
    filtered_im.save("leaf_grayscale.jpg")
