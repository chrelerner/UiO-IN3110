"""numpy implementation of image filters"""

from typing import Optional
import numpy as np
from PIL import Image


def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    gray_shape = (image.shape[0], image.shape[1])
    gray_image = np.empty(gray_shape)
    
    # Hint: use numpy slicing in order to have fast vectorized code
    
    red = image[:, :, 0]
    green = image[:, :, 1]
    blue = image[:, :, 2]
    
    weighted_sum = (red * 0.21) + (green * 0.72) + (blue * 0.07)
    gray_image[:, :] = weighted_sum[:]
    
    gray_image = gray_image.astype("uint8")
    # Return image (make sure it's the right type!)
    return gray_image


def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia filter to apply (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
    you may ignore it for Task 9)

    Returns:
        np.array: sepia_image
    """

    if not 0 <= k <= 1:
        # validate k (optional)
        raise ValueError(f"k must be between [0-1], got {k=}")

    width, height, channels = image.shape

    sepia_image = np.array((width, height, channels))

    # define sepia matrix (optional: with `k` tuning parameter for bonus task 13)
    
    sepia_matrix = np.array([
        [ 1 - ((1 - 0.393) * k), 0.769 * k, 0.189 * k],
        [ 0.349 * k, 1 - ((1 - 0.686) * k), 0.168 * k],
        [ 0.272 * k, 0.534 * k, 1 - ((1 - 0.131) * k)],
    ])

    # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    # use Einstein sum to apply pixel transform matrix
    # Apply the matrix filter
    sepia_image = np.einsum('ijk,lk->ijl', image, sepia_matrix)

    # Check which entries have a value greater than 255 and set it to 255 since we can not display values bigger than 255
    sepia_image[sepia_image > 255] = 255

    sepia_image = sepia_image.astype("uint8")
    # Return image (make sure it's the right type!)
    return sepia_image

if __name__ == "__main__":
    
    im = Image.open("test/leaf.jpg")
    #resized = im.resize((im.width // 2, im.height // 2))
    #data = np.asarray(resized)
    data = np.asarray(im)
    filtered_data = numpy_color2sepia(data, 1)
    filtered_im = Image.fromarray(filtered_data)
    filtered_im.save("test/leaf_sepia.jpg")
    
    