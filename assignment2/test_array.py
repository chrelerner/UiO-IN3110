"""
Tests for our array class
"""

from array_class import Array

# 1D tests (Task 4)


def test_str_1d():
    
    # Test 1 of size 5.
    array1 = Array((5,), 2, 4, 6, -8, 10)
    array1_correct_string = "[2, 4, 6, 8, 10]"
    assert (array1_correct_string == str(array1)), f"test_str_1d test 1: [2, 4, 6, 8, 10] expected, got {str(array1)}."
    
    # Test 2 of size 1.
    array2 = Array((1,), 7)
    array2_correct_string = "[7]"
    assert (array2_correct_string == str(array2)), f"test_str_1d test 2: [7] expected, got {str(array2)}."


def test_add_1d():
    
    # Testing of int scalar and array addition. Not testing commutative properties of array addition.
    int_array1 = Array((5,), 1, 3, 5, 7, 9)
    int_array2 = Array((5,), 1, -2, -3, 4, -5)
    int_scalar = 4
    
    int_result1 = int_array1 + int_array2 # Array1 + Array2
    int_result2 = int_array1 + int_scalar # Array1 + Scalar
    int_result3 = int_scalar + int_array1 # Scalar + Array1 | __radd__
    
    assert (str(int_result1) == "[2, 1, 2, 11, 4]"), f"test_add_1d int array: [2, 1, 2, 11, 4] expected, got {str(int_result1)}."
    assert (str(int_result2) == "[5, 7, 9, 11, 13]"), f"test_add_1d int scalar: [5, 7, 9, 11, 13] expected, got {str(int_result2)}."
    assert (int_result3 == int_result2), f"test_add_1d int _radd_: [5, 7, 9, 11, 13] expected, got {str(int_result3)}."
   
    
    # Testing of float scalar and array addition. Not testing commutative properties of array addition.
    float_array1 = Array((5,), 1.5, -3.0, 5.5, -1.3, 2.6)
    float_array2 = Array((5,), -2.3, -2.1, 3.0, -4.8, 5.2)
    float_scalar = 3.5
    
    float_result1 = float_array1 + float_array2 # Array1 + Array2
    float_result2 = float_array1 + float_scalar # Array1 + Scalar
    float_result3 = float_scalar + float_array1 # Scalar + Array1 | __radd__
    
    assert (str(float_result1) == "[-0.8, -5.1, 8.5, -6.1, 7.8]"), f"test_add_1d int array: [-0.8, -5.1, 8.5, -6.1, 7.8] expected, got {str(float_result1)}."
    assert (str(float_result2) == "[4.0, 0.5, 9.0, 2.2, 6.1]"), f"test_add_1d int scalar: [4.0, 0.5, 9.0, 2.2, 6.1] expected, got {str(float_result2)}."
    assert (float_result3 == float_result2), f"test_add_1d int _radd_: [5, 7, 9, 11, 13] expected, got {str(float_result3)}."
    
    
    # Testing of bool scalar and array addition. Should return NotImplemented.
    


def test_sub_1d():
    
    # Testing of int scalar and array subtraction.
    int_array1 = Array((5,), 1, 3, 5, 7, 9)
    int_array2 = Array((5,), 1, -2, -3, 4, -5)
    int_scalar = 4
    
    int_result1 = int_array1 - int_array2 # Array1 - Array2
    int_result2 = int_array1 - int_scalar # Array1 - Scalar
    int_result3 = int_scalar - int_array1 # Scalar - Array1 | __radd__   (Should return Array1 - Scalar)
    
    assert (str(int_result1) == "[2, 1, 2, 11, 4,]"), f"test_add_1d int array: [2, 1, 2, 11, 4,] expected, got {str(int_result1)}."
    assert (str(int_result2) == "[5, 7, 9, 11, 13,]"), f"test_add_1d int scalar: [5, 7, 9, 11, 13,] expected, got {str(int_result2)}."
    assert (int_result3 == int_result2), f"test_add_1d int _radd_: [5, 7, 9, 11, 13,] expected, got {str(int_result3)}."
   
    
    # Testing of float scalar and array subtraction.
    float_array1 = Array((5,), 1.5, -3.0, 5.5, -1.3, 2.6)
    float_array2 = Array((5,), -2.3, -2.1, 3.0, -4.8, 5.2)
    float_scalar = 3.5
    
    float_result1 = float_array1 - float_array2 # Array - Array
    float_result2 = float_array1 - float_scalar # Array - Scalar
    float_result3 = float_scalar - float_array1 # Scalar - Array | __radd__
    
    assert (str(float_result1) == "[-0.8, -5.1, 8.5, -6.1, 7.8,]"), f"test_add_1d int array: [-0.8, -5.1, 8.5, -6.1, 7.8,] expected, got {str(float_result1)}."
    assert (str(float_result2) == "[4.0, 0.5, 9.0, 2.2, 6.1,]"), f"test_add_1d int scalar: [4.0, 0.5, 9.0, 2.2, 6.1,] expected, got {str(float_result2)}."
    assert (float_result3 == float_result2), f"test_add_1d int _radd_: [5, 7, 9, 11, 13,] expected, got {str(float_result3)}."
    
    
    # Testing of bool scalar and array subtraction. Should return NotImplemented.


def test_mul_1d():
    
    # Testing of int scalar and array multiplication. Not testing commutative properties of array addition.
    int_array1 = Array((5,), 1, 3, 5, 7, 9)
    int_array2 = Array((5,), 1, -2, -3, 4, -5)
    int_scalar = 4
    
    int_result1 = int_array1 * int_array2 # Array1 * Array2
    int_result2 = int_array1 * int_scalar # Array1 * Scalar
    int_result3 = int_scalar * int_array1 # Scalar * Array1 | __radd__
    
    assert (str(int_result1) == "[2, 1, 2, 11, 4,]"), f"test_add_1d int array: [2, 1, 2, 11, 4,] expected, got {str(int_result1)}."
    assert (str(int_result2) == "[5, 7, 9, 11, 13,]"), f"test_add_1d int scalar: [5, 7, 9, 11, 13,] expected, got {str(int_result2)}."
    assert (int_result3 == int_result2), f"test_add_1d int _radd_: [5, 7, 9, 11, 13,] expected, got {str(int_result3)}."
   
    
    # Testing of float scalar and array multiplication. Not testing commutative properties of array addition.
    float_array1 = Array((5,), 1.5, -3.0, 5.5, -1.3, 2.6)
    float_array2 = Array((5,), -2.3, -2.1, 3.0, -4.8, 5.2)
    float_scalar = 3.5
    
    float_result1 = float_array1 * float_array2 # Array1 * Array2
    float_result2 = float_array1 * float_scalar # Array1 * Scalar
    float_result3 = float_scalar * float_array1 # Scalar * Array1 | __radd__
    
    assert (str(float_result1) == "[-0.8, -5.1, 8.5, -6.1, 7.8,]"), f"test_add_1d int array: [-0.8, -5.1, 8.5, -6.1, 7.8,] expected, got {str(float_result1)}."
    assert (str(float_result2) == "[4.0, 0.5, 9.0, 2.2, 6.1,]"), f"test_add_1d int scalar: [4.0, 0.5, 9.0, 2.2, 6.1,] expected, got {str(float_result2)}."
    assert (float_result3 == float_result2), f"test_add_1d int _radd_: [5, 7, 9, 11, 13,] expected, got {str(float_result3)}."
    
    
    # Testing of bool scalar and array multiplication. Should return NotImplemented.


def test_eq_1d():
    
    # Creating 3 different arrays for testing. Each will have its own copy.
    
    # Testing equality of arrays.
    
    # Testing unequality of arrays.
    
    
    pass


def test_same_1d():
    
    # Creating 3 different arrays for testing. Each will have its own copy.
    
    # Testing similarities of two arrays.
    
    # Testing similarities of array and scalar.
    
    
    pass


def test_smallest_1d():
    
    # Creating 4 different arrays for testing.
    
    
    pass


def test_mean_1d():
    
    # Creating 4 different arrays for testing.
    
    pass


# 2D tests (Task 6)


def test_add_2d():
    pass


def test_mult_2d():
    pass


def test_same_2d():
    pass


def test_mean_2d():
    pass


if __name__ == "__main__":
    """
    Note: Write "pytest" in terminal in the same folder as this file is in to run all tests
    (or run them manually by running this file).
    Make sure to have pytest installed (pip install pytest, or install anaconda).
    """

    # Task 4: 1d tests
    test_str_1d()
    test_add_1d()
    test_sub_1d()
    test_mul_1d()
    test_eq_1d()
    test_mean_1d()
    test_same_1d()
    test_smallest_1d()

    # Task 6: 2d tests
    test_add_2d()
    test_mult_2d()
    test_same_2d()
    test_mean_2d()
