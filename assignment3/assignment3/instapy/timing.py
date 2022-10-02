"""
Timing our filter implementations.

Can be executed as `python3 -m instapy.timing`

For Task 6.
"""
import time
import instapy
from . import io
from typing import Callable
import numpy as np


def time_one(filter_function: Callable, *arguments, calls: int = 3) -> float:
    """Return the time for one call

    When measuring, repeat the call `calls` times,
    and return the average.

    Args:
        filter_function (callable):
            The filter function to time
        *arguments:
            Arguments to pass to filter_function
        calls (int):
            The number of times to call the function,
            for measurement
    Returns:
        time (float):
            The average time (in seconds) to run filter_function(*arguments)
    """
    # run the filter function `calls` times

    measured_times = []
    
    for _ in range(calls):
        start_time = time.time()
        filter_function(*arguments)
        end_time = time.time()
        measured_times.append(end_time - start_time)
        
    average_time = sum(measured_times) / len(measured_times)
        
    
    # return the _average_ time of one call
    return average_time


def make_reports(filename: str = "test/rain.jpg", calls: int = 3):
    """
    Make timing reports for all implementations and filters,
    run for a given image.

    Args:
        filename (str): the image file to use
    """

    # load the image
    image = io.read_image(filename)
    
    # print the image name, width, height
    width, height = image.shape[:2]
    print(
        f"Timing performed using {filename}: {width}x{height}"
    )
    
    # iterate through the filters
    filter_names = ("color2gray", "color2sepia")
    for filter_name in filter_names:
        # get the reference filter function
        reference_filter = instapy.get_filter(filter_name, "python")
        
        # time the reference implementation
        reference_time = time_one(reference_filter, image)
        
        print(
            f"\nReference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=})"
        )
        # iterate through the implementations
        implementations = ("numpy", "numba")
        for implementation in implementations:
            filter = instapy.get_filter(filter_name, implementation)
            
            # time the filter
            filter_time = time_one(filter, image)
            
            # compare the reference time to the optimized time
            speedup = reference_time / filter_time
            print(
                f"Timing: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)"
            )


if __name__ == "__main__":
    # run as `python -m instapy.timing`
    make_reports()
