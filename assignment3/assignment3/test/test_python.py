from instapy.python_filters import python_color2gray, python_color2sepia

from instapy import io

import numpy.testing as nt

import numpy as np


def test_color2gray(image, reference_gray):
    
    # Runs color2gray.
    gray_image = python_color2gray(image)
    
    # Creates variables to be used in assertions.
    regular_shape = image.shape
    gray_shape = gray_image.shape
    
    regular_dtype = image.dtype
    gray_dtype = gray_image.dtype
    
    
    # Asserts shape and type
    assert regular_shape == gray_shape, f"Testing python_color2gray shape: {str(regular_shape)} expected, got {str(gray_shape)}"
    assert regular_dtype == gray_dtype, f"Testing python_color2gray type: {str(regular_dtype)} expected, got {str(gray_dtype)}"
    
    # Asserts pixel values.
    nt.assert_allclose(
        gray_image[0:2, 0:2], 
        reference_gray[0:2, 0:2], 
        rtol=1e-07, 
        atol=0, 
        equal_nan=True, 
        err_msg='Testing python_color2gray result: Resulting image not valid.',
    )


def test_color2sepia(image, reference_sepia):
    
    # Runs color2sepia.
    sepia_image = python_color2sepia(image)
    
    # Creates variables to be used in assertions.
    regular_shape = image.shape
    sepia_shape = sepia_image.shape
    
    regular_dtype = image.dtype
    sepia_dtype = sepia_image.dtype
    
    
    # Asserts shape and type
    assert regular_shape == sepia_shape, f"Testing python_color2sepia shape: {str(regular_shape)} expected, got {str(sepia_shape)}"
    assert regular_dtype == sepia_dtype, f"Testing python_color2sepia type: {str(regular_dtype)} expected, got {str(sepia_dtype)}"
    
    # Asserts pixel values.
    nt.assert_allclose(
        sepia_image[0:2, 0:2], 
        reference_sepia[0:2, 0:2], 
        rtol=1e-07, 
        atol=0, 
        equal_nan=True, 
        err_msg='Testing python_color2gray result: Resulting image not valid.',
    )

if __name__ == "__main__":
    
    image = io.read_image("rain.jpg")
    gray_image = io.read_image("rain_grayscale.jpg")
    sepia_image = io.read_image("rain.sepia.jpg")
    
    test_color2gray(image.copy(), gray_image)

    test_color2sepia(image.copy(), sepia_image)    
    