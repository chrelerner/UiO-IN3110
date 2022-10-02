from instapy.numpy_filters import numpy_color2gray, numpy_color2sepia

import numpy.testing as nt

import conftest as ct


def test_color2gray(image, reference_gray):
    """Tests the numpy implementations of color2gray."""
    
    # Runs color2gray.
    gray_image = numpy_color2gray(image)
    
    # Creates variables to be used in assertions.
    regular_shape = image.shape
    gray_shape = gray_image.shape
    
    regular_dtype = image.dtype
    gray_dtype = gray_image.dtype
    
    
    # Asserts shape and type. Shape for numpy_color2gray should be 2-dimensional.
    assert regular_shape[:2] == gray_shape, f"Testing python_color2gray shape: {str(regular_shape)} expected, got {str(gray_shape)}"
    assert regular_dtype == gray_dtype, f"Testing python_color2gray type: {str(regular_dtype)} expected, got {str(gray_dtype)}"
    
    # Asserts pixel values.
    nt.assert_allclose(
        gray_image[:2, :2], 
        reference_gray[:2, :2, 0],  # Must be restricted to one color channel.
        rtol=1e-07, 
        atol=0, 
        equal_nan=True, 
        err_msg='Testing python_color2gray result: Resulting image not valid.',
    )


def test_color2sepia(image, reference_sepia):
    """Tests the numpy implementations of color2sepia."""
    
    # Runs color2sepia.
    sepia_image = numpy_color2sepia(image)
    
    # Creates variables to be used in assertions.
    regular_shape = image.shape
    sepia_shape = sepia_image.shape
    
    regular_dtype = image.dtype
    sepia_dtype = sepia_image.dtype
    
    
    # Asserts shape and type.
    assert regular_shape == sepia_shape, f"Testing python_color2sepia shape: {str(regular_shape)} expected, got {str(sepia_shape)}"
    assert regular_dtype == sepia_dtype, f"Testing python_color2sepia type: {str(regular_dtype)} expected, got {str(sepia_dtype)}"
    
    # Asserts pixel values.
    nt.assert_allclose(
        sepia_image[:2, :2], 
        reference_sepia[:2, :2], 
        rtol=0, 
        equal_nan=True, 
        err_msg='Testing python_color2sepia result: Resulting image not valid.',
    )
    
if __name__ == "__main__":
    
    # Generates a random image and its filtered versions.
    original_image = ct.random_image()
    reference_gray = ct.reference_gray()
    reference_sepia = ct.reference_sepia()
    
    test_color2gray(original_image.copy(), reference_gray)
    
    test_color2sepia(original_image.copy(), reference_sepia)
