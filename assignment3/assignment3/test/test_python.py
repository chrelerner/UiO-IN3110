from instapy.python_filters import python_color2gray, python_color2sepia
from PIL import Image
import numpy as np


def test_color2gray(image):
    
    # Runs color2gray.
    image_data = np.asarray(image)
    image_grayscale_data = python_color2gray(image_data)
    
    # Creates variables to be used in assertions.
    regular_shape = image_data.shape
    gray_shape = image_grayscale_data.shape
    
    regular_dtype = image_data.dtype
    gray_dtype = image_grayscale_data.dtype
    
    
    # Asserts shape and type
    assert regular_shape == gray_shape, f"Testing python_color2gray shape: {str(regular_shape)} expected, got {str(gray_shape)}"
    assert regular_dtype == gray_dtype, f"Testing python_color2gray type: {str(regular_dtype)} expected, got {str(gray_dtype)}"
    
    # Creates a grayscale picture using PIL, to compare with the result from color2gray
    PIL_image_grayscale_data = image.convert('L')
    
    assert np.allclose(image_grayscale_data[0:2, 0:2, :], PIL_image_grayscale_data[0:2, 0:2, :]) == True, "Testing python_color2gray result: Resulting image not valid."


def test_color2sepia(image):
    # Runs color2sepia.
    image_data = np.asarray(image)
    image_sepia_data = python_color2sepia(image_data)
    
    # Creates variables to be used in assertions.
    regular_shape = image_data.shape
    sepia_shape = image_sepia_data.shape
    
    regular_dtype = image_data.dtype
    sepia_dtype = image_sepia_data.dtype
    
    
    # Asserts shape and type
    assert regular_shape == sepia_shape, f"Testing python_color2sepia shape: {str(regular_shape)} expected, got {str(sepia_shape)}"
    assert regular_dtype == sepia_dtype, f"Testing python_color2sepia type: {str(regular_dtype)} expected, got {str(sepia_dtype)}"
    
    # Creates a grayscale picture using PIL, to compare with the result from color2sepia
    PIL_image_sepia_data = image.convert('L')
    
    assert np.allclose(image_sepia_data[0:2, 0:2, :], PIL_image_sepia_data[0:2, 0:2, :]) == True, "Testing python_color2sepia result: Resulting image not valid."
