Information on the implementation of the Array-class:

The class has been implemented for n-dimensional use, however only a few methods vary noticably from a 1d implementation.
The rest of the methods work exactly as they used to for 1d-arrays. 
Many of the methods in the Array-class share similar code.



Information on the unit tests:

The unit tests include detailed comments on what is being tested where. The unit tests do not
include all possible situations for the array, only the most important situations.
Also, the unit tests do not check for exceptions where they should be raised, they simply
check the standard expected values for proper method arguments.



Information on how to run the scripts:

I haven't made any separate files other than the ones specified in the assignment text. This means that the
scripts can be run simply by being in the same folder as the two files in a terminal and writing "pytest", or
running "test_array.py" directly.