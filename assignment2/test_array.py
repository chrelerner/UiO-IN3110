"""
Tests for our array class
"""

from array_class import Array

# 1D tests (Task 4)


def test_str_1d():
    
    # Testing arrays of ints.
    int_array1 = Array((5,), 2, 4, 6, -8, 10)
    int_array1_correct_string = "[2, 4, 6, -8, 10]"
    assert (int_array1_correct_string == str(int_array1)), f"test_str_1d int test 1: [2, 4, 6, -8, 10] expected, got {str(int_array1)}."
    
    int_array2 = Array((1,), 7)
    int_array2_correct_string = "[7]"
    assert (int_array2_correct_string == str(int_array2)), f"test_str_1d int test 2: [7] expected, got {str(int_array2)}."
    
    
    # Testing arrays of floats.
    float_array1 = Array((3,), 5.8, 2.76, 4.43)
    float_array1_correct_string = "[5.8, 2.76, 4.43]"
    assert (float_array1_correct_string == str(float_array1)), f"test_str_1d float test 1: [5.8, 2.76, 4.43] expected, got {str(float_array1)}."

    float_array2 = Array((7,), 5.67, 3.46, 4.43, 8.54, -3.2, 4.2, -1.05)
    float_array2_correct_string = "[5.67, 3.46, 4.43, 8.54, -3.2, 4.2, -1.05]"
    assert (float_array2_correct_string == str(float_array2)), f"test_str_1d float test 2: [5.67, 3.46, 4.43, 8.54, -3.2, 4.2, -1.05] expected, got {str(float_array2)}."
    
    
    # Testing arrays of bools.
    bool_array1 = Array((4,), True, True, False, False)
    bool_array1_correct_string = "[True, True, False, False]"
    assert (bool_array1_correct_string == str(bool_array1)), f"test_str_1d bool test 1: [True, True, False, False] expected, got {str(bool_array1)}."
    
    bool_array2 = Array((6,), True, True, False, True, False, True)
    bool_array2_correct_string = "[True, True, False, True, False, True]"
    assert (bool_array2_correct_string == str(bool_array2)), f"test_str_1d bool test 2: [True, True, False, True, False, True] expected, got {str(bool_array2)}."    
    

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
    
    assert (str(float_result1) == "[-0.8, -5.1, 8.5, -6.1, 7.8]"), f"test_add_1d float array: [-0.8, -5.1, 8.5, -6.1, 7.8] expected, got {str(float_result1)}."
    assert (str(float_result2) == "[5.0, 0.5, 9.0, 2.2, 6.1]"), f"test_add_1d float scalar: [4.0, 0.5, 9.0, 2.2, 6.1] expected, got {str(float_result2)}."
    assert (float_result3 == float_result2), f"test_add_1d float _radd_: [4.0, 0.5, 9.0, 2.2, 6.1] expected, got {str(float_result3)}."
    
    
    # Testing of bool scalar and array addition. Should return NotImplemented.
    bool_array1 = Array((5,), True, True, True, False, False)
    bool_array2 = Array((5,), False, False, True, True, False)
    bool_array3 = Array((5,), 1, 2, 3, 4, 5)
    bool_scalar = True
    
    bool_result1 = bool_array1.__add__(bool_array2)
    bool_result2 = bool_array1.__add__(bool_scalar)
    bool_result3 = bool_array3.__add__(bool_array1)
    
    assert bool_result1 == NotImplemented, f"test_add_1d bool test 1: NotImplemented expected, got {bool_result1}"
    assert bool_result2 == NotImplemented, f"test_add_1d bool test 2: NotImplemented expected, got {bool_result2}"
    assert bool_result3 == NotImplemented, f"test_add_1d bool test 3: NotImplemented expected, got {bool_result3}"
    


def test_sub_1d():
    
    # Testing of int scalar and array subtraction.
    int_array1 = Array((3,), 1, 3, 5)
    int_array2 = Array((3,), 1, -2, -3)
    int_scalar = 4
    
    int_result1 = int_array1 - int_array2 # Array1 - Array2
    int_result2 = int_array1 - int_scalar # Array1 - Scalar
    int_result3 = int_scalar - int_array1 # Scalar - Array1 | __rsub__   (Should return Array1 - Scalar)
    
    assert (str(int_result1) == "[0, 5, 8]"), f"test_sub_1d int array: [0, 5, 8] expected, got {str(int_result1)}."
    assert (str(int_result2) == "[-3, -1, 1]"), f"test_sub_1d int scalar: [-3, -1, 1] expected, got {str(int_result2)}."
    assert (int_result3 == int_result2), f"test_sub_1d int _rsub_: [-3, -6, -7] expected, got {str(int_result3)}."
   
    
    # Testing of float scalar and array subtraction.
    float_array1 = Array((6,), 1.5, -3.0, 5.5, -1.3, 2.6, 4.0)
    float_array2 = Array((6,), -2.3, -2.1, 3.0, -4.8, 5.2, 2.0)
    float_scalar = 3.5
    
    float_result1 = float_array1 - float_array2 # Array1 - Array2
    float_result2 = float_array1 - float_scalar # Array1 - Scalar
    float_result3 = float_scalar - float_array1 # Scalar - Array1 | __rsub__   (Should return Array1 - Scalar)
    
    assert (str(float_result1) == "[3.8, -0.9, 2.5, 3.5, -2.6, 2.0]"), f"test_sub_1d float array: [3.8, -0.9, 2.5, 3.5, -2.6, 2.0] expected, got {str(float_result1)}."
    assert (str(float_result2) == "[-2.0, -6.5, 2.0, -4.8, -0.9, 0.5]"), f"test_sub_1d float scalar: [-1.5, -6.5, 2.0, -4.8, -0.9, 0.5] expected, got {str(float_result2)}."
    assert (float_result3 == float_result2), f"test_sub_1d float _rsub_: [-1.5, -6.5, 2.0, -4.8, -0.9, 0.5] expected, got {str(float_result3)}."
    
    
    # Testing of bool scalar and array subtraction. Should return NotImplemented.
    bool_array1 = Array((5,), True, True, True, False, False)
    bool_array2 = Array((5,), False, False, True, True, False)
    bool_array3 = Array((5,), 1, 2, 3, 4, 5)
    bool_scalar = True
    
    bool_result1 = bool_array1.__sub__(bool_array2)
    bool_result2 = bool_array1.__sub__(bool_scalar)
    bool_result3 = bool_array3.__sub__(bool_array1)
    
    assert bool_result1 == NotImplemented, f"test_sub_1d bool test 1: NotImplemented expected, got {bool_result1}"
    assert bool_result2 == NotImplemented, f"test_sub_1d bool test 2: NotImplemented expected, got {bool_result2}"
    assert bool_result3 == NotImplemented, f"test_sub_1d bool test 3: NotImplemented expected, got {bool_result3}"


def test_mul_1d():
    
    # Testing of int scalar and array multiplication. Not testing commutative properties of array addition.
    int_array1 = Array((4,), 1, 3, 5, 7)
    int_array2 = Array((4,), 1, -2, -3, 4)
    int_scalar = 4
    
    int_result1 = int_array1 * int_array2 # Array1 * Array2
    int_result2 = int_array1 * int_scalar # Array1 * Scalar
    int_result3 = int_scalar * int_array1 # Scalar * Array1 | __rmul__
    
    assert (str(int_result1) == "[1, -6, -15, 28]"), f"test_mul_1d int array: [1, -6, -15, -28] expected, got {str(int_result1)}."
    assert (str(int_result2) == "[4, 12, 20, 28]"), f"test_mul_1d int scalar: [4, 12, 20, 28] expected, got {str(int_result2)}."
    assert (int_result3 == int_result2), f"test_mul_1d int _rmul_: [4, 12, 20, 28] expected, got {str(int_result3)}."
   
    
    # Testing of float scalar and array multiplication. Not testing commutative properties of array addition.
    float_array1 = Array((5,), 1.5, -3.0, 5.5, -1.3, 2.6)
    float_array2 = Array((5,), -2.3, -2.1, 3.0, -4.8, 5.2)
    float_scalar = 3.5
    
    float_result1 = float_array1 * float_array2 # Array1 * Array2
    float_result2 = float_array1 * float_scalar # Array1 * Scalar
    float_result3 = float_scalar * float_array1 # Scalar * Array1 | __rmul__
    
    assert (str(float_result1) == "[-3.45, 6.3, 16.5, 6.24, 13.52]"), f"test_mul_1d float array: [-3.45, 6.3, 16.5, 6.24, 13.52] expected, got {str(float_result1)}."
    assert (str(float_result2) == "[5.25, -10.5, 19.25, -4.55, 9.1]"), f"test_mul_1d float scalar: [5.25, -10.5, 19.25, -4.55, 9.1] expected, got {str(float_result2)}."
    assert (float_result3 == float_result2), f"test_mul_1d float _rmul_: [5.25,-10.5,  19.25, -4.55, 9.1] expected, got {str(float_result3)}."
    
    
    # Testing of bool scalar and array multiplication. Should return NotImplemented.
    bool_array1 = Array((5,), True, True, True, False, False)
    bool_array2 = Array((5,), False, False, True, True, False)
    bool_array3 = Array((5,), 1, 2, 3, 4, 5)
    bool_scalar = True
    
    bool_result1 = bool_array1.__mul__(bool_array2)
    bool_result2 = bool_array1.__mul__(bool_scalar)
    bool_result3 = bool_array3.__mul__(bool_array1)
    
    assert bool_result1 == NotImplemented, f"test_mul_1d bool test 1: NotImplemented expected, got {bool_result1}"
    assert bool_result2 == NotImplemented, f"test_mul_1d bool test 2: NotImplemented expected, got {bool_result2}"
    assert bool_result3 == NotImplemented, f"test_mul_1d bool test 3: NotImplemented expected, got {bool_result3}"
    

def test_eq_1d():
    
    # Creating 6 different arrays for testing. The first 3 will have their own copy.
    array1 = Array((3,), 1, 2, 3)
    array2 = Array((5,), 3.2, 5.0, 2.1, 1.7, 4.6)
    array3 = Array((4,), True, False, True, False)
    
    array4 = Array((5,), 5, 5, 7, 9, 1)
    array5 = Array((4,), 1.3, 4.4, 3.0, 7.1)
    array6 = Array((3,), False, False, True)
    
    copy_array1 = Array((3,), 1, 2, 3)
    copy_array2 = Array((5,), 3.2, 5.0, 2.1, 1.7, 4.6)
    copy_array3 = Array((4,), True, False, True, False)
    
    
    # Testing equality of arrays.
    equal_result1 = array1 == copy_array1
    equal_result2 = array2 == copy_array2
    equal_result3 = array3 == copy_array3
        
    assert equal_result1 == True, f"test_eq_1d equality 1: True expected, got {str(equal_result1)}."
    assert equal_result2 == True, f"test_eq_1d equality 2: True expected, got {str(equal_result2)}."
    assert equal_result3 == True, f"test_eq_1d equality 3: True expected, got {str(equal_result3)}."
    
    
    # Testing inequality of arrays.
    unequal_result1 = array1 == array6
    unequal_result2 = array2 == array4
    unequal_result3 = array3 == array5
    
    assert unequal_result1 == False, f"test_eq_1d inequality 1: False expected, got {str(unequal_result1)}."
    assert unequal_result2 == False, f"test_eq_1d inequality 2: False expected, got {str(unequal_result2)}."
    assert unequal_result3 == False, f"test_eq_1d inequality 3: False expected, got {str(unequal_result3)}."


def test_same_1d():
    
    # Creating 6 different arrays for testing. Some will be slightly similar to eachother.
    array1 = Array((5,), 5, 5, 7, 9, 1)
    array2 = Array((4,), 1.3, 4.4, 3.0, 7.1)
    array3 = Array((6,), False, False, True, True, True, False)
    
    array4 = Array((5,), 5, 2, 1, 9, 7)
    array5 = Array((4,), 1.2, 4.4, 5.6, -3.5)
    array6 = Array((6,), False, False, False, True, False, True)
    
    
    # Testing similarities between two arrays.
    array_result1 = array1.is_equal(array4)
    array_result2 = array2.is_equal(array5)
    array_result3 = array3.is_equal(array6)
    
    assert (str(array_result1) == "[True, False, False, True, False]"), f"test_same_1d array 1: [True, False, False, True, False] expected, got {str(array_result1)}"
    assert (str(array_result2) == "[False, True, False, False]"), f"test_same_1d array 2: [False, True, False, False] expected, got {str(array_result2)}"
    assert (str(array_result3) == "[True, True, False, True, False, False]"), f"test_same_1d array 3: [True, False, False, True, False] expected, got {str(array_result3)}"
    
    
    # Testing similarities between array and scalar.
    scalar_result1 = array1.is_equal(5)
    scalar_result2 = array2.is_equal(7.1)
    scalar_result3 = array3.is_equal(False)
    
    assert (str(scalar_result1) == "[True, True, False, False, False]"), f"test_same_1d scalar 1: [True, True, False, False, False] expected, got {str(array_result1)}"
    assert (str(scalar_result2) == "[False, False, False, True]"), f"test_same_1d scalar 2: [False, False, False, True] expected, got {str(scalar_result2)}"
    assert (str(scalar_result3) == "[True, True, False, False, False, True]"), f"test_same_1d scalar 3: [True, True, False, False, False, True] expected, got {str(scalar_result3)}"
    


def test_smallest_1d():
    
    # Creating 3 different arrays for testing.
    array1 = Array((5,), 4, 5, 1, 7, 9)
    array2 = Array((6,), 1, 4, -2, 6, 9, -5)
    array3 = Array((3,), 3.4, 1.7, 2.1)
    
    result1 = array1.min_element()
    result2 = array2.min_element()
    result3 = array3.min_element()
    
    assert (result1 == 1), f"test_smallest_1d 1: 1 expected, got {result1}."
    assert (result2 == -5), f"test_smallest_1d 2: -5 expected, got {result2}."
    assert (result3 == 1.7), f"test_smallest_1d 3: 1.7 expected, got {result3}."
    


def test_mean_1d():
    
    # Creating 3 different arrays for testing.
    array1 = Array((5,), 4, 5, 1, 7, 9)
    array2 = Array((6,), 1, 4, -2, 6, 9, -5)
    array3 = Array((3,), 3.4, 1.7, 2.1)
    
    result1 = array1.mean_element()
    result2 = array2.mean_element()
    result3 = array3.mean_element()
    
    assert (result1 == 5.2), f"test_mean_1d 1: 5.2 expected, got {result1}."
    assert (result2 == 2.17), f"test_mean_1d 2: 2.17 expected, got {result2}."
    assert (result3 == 2.4), f"test_mean_1d 3: 2.4 expected, got {result3}."


# 2D tests (Task 6)


def test_add_2d():

    # Testing of int scalar and array addition. Not testing commutative properties of array addition.
    int_array1 = Array((2, 3), 1, -2, 3, -4, 5, -6)
    int_array2 = Array((2, 3), -6, 5, -4, 3, -2, 1)
    int_scalar = 4
    
    int_result1 = int_array1 + int_array2 # Array1 + Array2
    int_result2 = int_array1 + int_scalar # Array1 + Scalar
    int_result3 = int_scalar + int_array1 # Scalar + Array1 | __radd__
    
    assert (str(int_result1) == "[[-5, 3, -1], [-1, 3, -5]]"), f"test_add_2d int array: [[-5, 3, 1], [-1, 3, -5]] expected, got {str(int_result1)}."
    assert (str(int_result2) == "[[5, 2, 7], [0, 9, -2]]"), f"test_add_2d int scalar: [[5, 2, 7], [0, 9, -2]] expected, got {str(int_result2)}."
    assert (int_result3 == int_result2), f"test_add_2d int _radd_: [[5, 2, 7], [0, 9, -2]] expected, got {str(int_result3)}."
   
    
    # Testing of float scalar and array addition. Not testing commutative properties of array addition.
    float_array1 = Array((3, 2), 1.5, -3.0, 5.5, -1.3, 2.6, 7.3)
    float_array2 = Array((3, 2), -2.3, -2.1, 3.0, -4.8, 5.2, 8.2)
    float_scalar = 3.5
    
    float_result1 = float_array1 + float_array2 # Array1 + Array2
    float_result2 = float_array1 + float_scalar # Array1 + Scalar
    float_result3 = float_scalar + float_array1 # Scalar + Array1 | __radd__
    
    assert (str(float_result1) == "[[-0.8, -5.1], [8.5, -6.1], [7.8, 15.5]]"), f"test_add_2d float array: [[-0.8, -5.1], [8.5, -6.1], [7.8, 15.5]] expected, got {str(float_result1)}."
    assert (str(float_result2) == "[[5.0, 0.5], [9.0, 2.2], [6.1, 10.8]]"), f"test_add_2d float scalar: [[5.0, 0.5], [9.0, 2.2], [6.1, 10.8]] expected, got {str(float_result2)}."
    assert (float_result3 == float_result2), f"test_add_2d float _radd_: [[5.0, 0.5], [9.0, 2.2], [6.1, 10.8]] expected, got {str(float_result3)}."
    
    
    # Testing of bool scalar and array addition. Should return NotImplemented.
    bool_array1 = Array((2, 2), True, True, True, False)
    bool_array2 = Array((2, 2), False, False, True, True)
    bool_array3 = Array((2, 2), 1, 2, 3, 4)
    bool_scalar = True
    
    bool_result1 = bool_array1.__add__(bool_array2)
    bool_result2 = bool_array1.__add__(bool_scalar)
    bool_result3 = bool_array3.__add__(bool_array1)
    
    assert bool_result1 == NotImplemented, f"test_add_1d bool test 1: NotImplemented expected, got {bool_result1}"
    assert bool_result2 == NotImplemented, f"test_add_1d bool test 2: NotImplemented expected, got {bool_result2}"
    assert bool_result3 == NotImplemented, f"test_add_1d bool test 3: NotImplemented expected, got {bool_result3}"
    


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
