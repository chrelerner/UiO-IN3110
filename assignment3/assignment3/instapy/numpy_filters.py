"""numpy implementation of image filters"""

from typing import Optional
import numpy as np
from PIL import Image


def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale
    
    The returned array of this function has a shape of two dimensions,
    not three like the input-array.

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    gray_shape = image.shape[:2]
    gray_image = np.empty(gray_shape)
    
    # Goes through all pixels and applies a grayscale transform.
    red = image[:, :, 0]
    green = image[:, :, 1]
    blue = image[:, :, 2]
    
    weighted_sum = (red * 0.21) + (green * 0.72) + (blue * 0.07)
    gray_image[:] = weighted_sum
    
    gray_image = gray_image.astype("uint8")
    return gray_image


def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia filter to apply (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    Returns:
        np.array: sepia_image
    """

    if not 0 <= k <= 1:
        # validate k (optional)
        raise ValueError(f"k must be between [0-1], got {k=}")

    sepia_image = np.empty_like(image)

    # Defines a tunable sepia-matrix using the 'k' variable.    
    sepia_matrix = np.array([
        [ 1 - ((1 - 0.393) * k), 0.769 * k, 0.189 * k],
        [ 0.349 * k, 1 - ((1 - 0.686) * k), 0.168 * k],
        [ 0.272 * k, 0.534 * k, 1 - ((1 - 0.131) * k)],
    ])

    sepia_image = np.einsum('ijk,lk->ijl', image, sepia_matrix)  # Applies sepia-filter using Einstein sum.
    sepia_image[sepia_image > 255] = 255

    sepia_image = sepia_image.astype("uint8")
    return sepia_image

if __name__ == "__main__":
    
    im = Image.open("test/rain.jpg")
    #resized = im.resize((im.width // 2, im.height // 2))
    #data = np.asarray(resized)
    data = np.asarray(im)
    filtered_data = numpy_color2sepia(data)
    filtered_im = Image.fromarray(filtered_data)
    filtered_im.save("test/rain_sepia.jpg")
    
    filtered_data = numpy_color2gray(data)
    filtered_im = Image.fromarray(filtered_data)
    filtered_im.save("test/rain_grayscale.jpg")
    
    