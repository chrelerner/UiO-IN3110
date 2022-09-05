"""
Array class for assignment 2
"""

class Array:

    def __init__(self, shape, *values):
        """Initialize an array of 1-dimensionality. Elements can only be of type:

        - int
        - float
        - bool

        Make sure the values and shape are of the correct type.

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either int, float or boolean.

        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """

        # Checks if the values are of valid types
        
        if not isinstance(shape, tuple):
            # Returns informative TypeError.
            raise TypeError("Shape argument is not a tuple.\n")
                
        for element in values:
            
            if not isinstance(element, int):
                if not isinstance(element, float):
                    if not isinstance(element, bool):
                        #Returns informative TypeError
                        raise TypeError("Argument contained value of type not allowed.\n")
        
        values_type = type(values[0])
        
        for element in values:
            
            if type(element) != values_type:
                # Returns informative ValueError.
                raise ValueError("Array-elements given as argument do not share the same type.\n")
    
    

        # Checks that the amount of values corresponds to the shape
        
        if shape[0] != len(values):
            # Returns informative ValueError
            raise ValueError("Amount of values given does not correspond to the shape.\n")



        # Set class-variables
        self.shape = shape
        self.value_list = []
        self.values_type = values_type
        
        for element in values:
            self.value_list.append(element)
            
            
    # This method returns the element at the given index of the array.
    def __getitem__(self, index):
        
        if isinstance(index, int):
            return self.value_list[index]
        else:
            # Return informative TypeError.
            raise TypeError("Index argument should be of type int.\n")
        
        
        
    # Fix this method with a better representation, like Array((5,), 1, 2, 3, 4, 5).
    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        result = "["
        
        for element in self.value_list:
            result += element + ", "
        result += "]"
        
        print(result)
        

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """

        # check that the method supports the given arguments (check for data type and shape of array)
        # if the array is a boolean you should return NotImplemented

        if self.values_type == "bool":
            return NotImplemented
        
        # Checks that 'other' is a scalar OR an array of the same shape as self.
        # Returns NotImplemented if not.
        if not isinstance(other, (int, float)):
            if not isinstance(other, Array):
                return NotImplemented
            if other.shape != self.shape:
                return NotImplemented
        
        
        # Perform addition by scalar.
        if isinstance(other, (int, float)):
            
            for i in range(len(self.value_list)):
                self.value_list[i] += other
                
        # Performs addition by array.
        else:
            
            for i in range(len(self.value_list)):
                self.value_list[i] += other.value_list[i]
        
        


    # Same implementation as __add__.
    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
        pass

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        pass

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        pass

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """
        pass

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.

        """

        pass

    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """

        pass

    def mean_element(self):
        """Returns the mean value of an array

        Only needs to work for type int and float (not boolean).

        Returns:
            float: the mean value
        """

        pass
