"""Command-line (script) interface to instapy"""

import argparse
import sys

import numpy as np
from PIL import Image

import instapy
from . import io


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
) -> None:
    """Run the selected filter"""
    # load the image from a file
    im = Image.open(file)
    if scale != 1:
        # Resize image, if needed
        im = im.resize((im.width // scale, im.height // scale))

    # Apply the filter
    image = np.asarray(im)
    filter_method = instapy.get_filter(filter, implementation)
    filtered = filter_method(image)
    if out_file:
        # save the file
        io.write_image(filtered, out_file)
    else:
        # not asked to save, display it instead
        io.display(filtered)


def display_runtime() -> None:
    ...


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")
    parser.add_argument("-o", "--out", help="The output filename")

    # Add required arguments
    parser.add_argument("-g", "--gray", help="Select gray filter") # flag
    parser.add_argument("-se", "--sepia", help="Select sepia filter") # flag
    parser.add_argument("-sc", "--scale", help="Scale factor to resize image")
    parser.add_argument("-i", "--implementation", help="The implementation")
    
    # Bonustask - Use separate function and not run_filter().
    parser.add_argument("-r", "--runtime", help="Display average runtime for filter")

    # parse arguments and call run_filter
    args = parser.parge_args()
    
