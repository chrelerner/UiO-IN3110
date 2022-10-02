<h1>Instapy</h1>

This package contains filtering functions that will transform your image of choice
into a dramatic grayscale version, or a nostalgic sepia version.
Each filter has been implemented three separate times with different approaches, using
Python, NumPy and numba.


<h2>Instructions on how to install:</h2>

Download the folder in which this README file is in, and navigate to said folder in a terminal.

Now write "python3 -m pip install .", and Instapy should begin installing.


<h2>Instructions on how to run:</h2>

To run Instapy, simply type in your terminal either "python3 -m instapy 'filename'",
or "instapy 'filename'", where 'filename' is the picture you want filtered. 
Follow this up with flags of your choice, from this list of flags:

    - File to store filtered image:   -o OUT, --out OUT
    - Use dramatic grayscale filter:  -g, --gray
    - Use nostalgic sepia filter:     -se, --sepia
    - Scale the image down:           -sc SCALE, --scale SCALE
    - Use specified implementation:   -i {python, numba, numpy}, --implementation {python, numpy, numba}
    - Display average runtime:        -r, --runtime
    
All of these listed flags are optional. If you do not specify an output file, the filtered image
will instead be displayed.

The default filter used without specifying a filter is dramatic grayscale, and default implementation is Python.