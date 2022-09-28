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

    sepia_image = ...

    # define sepia matrix (optional: with `k` tuning parameter for bonus task 13)
    sepia_matrix = ...

    # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    # use Einstein sum to apply pixel transform matrix
    # Apply the matrix filter
    sepia_image = ...

    # Check which entries have a value greater than 255 and set it to 255 since we can not display values bigger than 255
    ...

    # Return image (make sure it's the right type!)
    return sepia_image

if __name__ == "__main__":
    
    im = Image.open("leaf.jpg")
    resized = im.resize((im.width // 2, im.height // 2))
    leaf_data = np.asarray(resized)
    leaf_grayscale_data = numpy_color2gray(leaf_data)
    leaf_grayscale = Image.fromarray(leaf_grayscale_data)
    leaf_grayscale.save("leaf_grayscale.jpg")
    
    
    im = Image.open("rain_hand.jpg")
    resized = im.resize((im.width // 2, im.height // 2))
    rain_hand_data = np.asarray(resized)
    rain_hand_grayscale_data = numpy_color2gray(rain_hand_data)
    rain_hand_grayscale = Image.fromarray(rain_hand_grayscale_data)
    rain_hand_grayscale.save("rain_hand_grayscale.jpg")
    
    