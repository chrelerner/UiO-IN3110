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
    
    sepia_matrix = np.array([
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ])
    
    
    # Iterate through the pixels
    # applying the sepia matrix
    
    for i in range( len(image) ):
        row = image[i]
        for j in range(len(row) ):
            pixel = row[j]
            
            red, green, blue = pixel[0], pixel[1], pixel[2]
            
            sepia_red = sepia_matrix[0][0] * red + sepia_matrix[0][1] * green + sepia_matrix[0][2] * blue
            sepia_green = sepia_matrix[1][0] * red + sepia_matrix[1][1] * green + sepia_matrix[1][2] * blue 
            sepia_blue = sepia_matrix[2][0] * red + sepia_matrix[2][1] * green + sepia_matrix[2][2] * blue
            
            sepia_image[i][j][0] = min(255, sepia_red)
            sepia_image[i][j][1] = min(255, sepia_green)
            sepia_image[i][j][2] = min(255, sepia_blue)
            

    sepia_image = sepia_image.astype("uint8")

    # Return image
    # don't forget to make sure it's the right type!
    return sepia_image

if __name__ == "__main__":
    
    im = Image.open("../test/rain.jpg")
    #resized = im.resize((im.width // 2, im.height // 2))
    #data = np.asarray(resized)
    data = np.asarray(im)
    filtered_data = python_color2sepia(data)
    filtered_im = Image.fromarray(filtered_data)
    filtered_im.save("rain_sepia.jpg")
    
    
    
