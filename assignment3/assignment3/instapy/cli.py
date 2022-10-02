"""Command-line (script) interface to instapy"""

import argparse
import sys

import numpy as np
from PIL import Image

import instapy
from . import io

import time


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
) -> None:
    """Run the selected filter"""
    
    # Loads the image from a file and scales it if specified
    im = Image.open(file)
    if scale != 1:
        im = im.resize((im.width // scale, im.height // scale))

    # Transforms 'im' to nparray, and applies the filter.
    image = np.asarray(im)
    filter_function = instapy.get_filter(filter, implementation)
    filtered = filter_function(image)
    
    # Saves or displays the filtered image.
    if out_file:
        io.write_image(filtered, out_file)
    else:
        io.display(filtered)


def display_runtime(
    file: str,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,        
) -> None:
    
    # Loads the image from a file and scales it if specified
    im = Image.open(file)
    if scale != 1:
        im = im.resize((im.width // scale, im.height // scale))
        
    # Transforms 'im' to nparray, and applies the filter 3 times, timing it.
    image = np.asarray(im)
    filter_function = instapy.get_filter(filter, implementation)
    
    measured_times = []
    for _ in range(3):
        start_time = time.time()
        filter_function(image)
        end_time = time.time()
        measured_times.append(end_time - start_time)
        
    runtime = sum(measured_times) / len(measured_times)
    
    print(f"Average time over 3 runs: {runtime}s")


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    # Filename is positional and required
    parser.add_argument("file", required=True, help="The filename to apply filter to")
    parser.add_argument("-o", "--out", help="The output filename")

    # Adds mutually exclusive arguments for color2gray and color2sepia.
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-g", "--gray", action="store_true", help="Select gray filter") # flag
    group.add_argument("-se", "--sepia", action="store_true", help="Select sepia filter") # flag
    
    parser.add_argument("-sc", "--scale", type=int, default=1, help="Scale factor to resize image")
    parser.add_argument("-i", "--implementation", type=str, default="python", choices=["python", "numpy", "numba"], help="The implementation")
    parser.add_argument("-r", "--runtime", action="store_true", help="Display average runtime for filter")

    # Parses the arguments and calls run_filter, and display_runtime if specified.
    args = parser.parge_args()
    
    if args.sepia:
        run_filter(file = args.file, out_file = args.out, implementation = args.implementation, filter = "color2sepia", scale = args.scale)
        
        if args.runtime:
            display_runtime(file = args.file, implementation = args.implementation, filter = "color2sepia", scale = args.scale)
            
    else:
        run_filter(file = args.file, out_file = args.out, implementation = args.implementation, filter = "color2gray", scale = args.scale)
        
        if args.runtime:
            display_runtime(file = args.file, implementation = args.implementation, filter = "color2gray", scale = args.scale)
    
        
        
        
    
