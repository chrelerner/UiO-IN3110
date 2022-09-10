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

        # Checks if 'shape' is a tuple.
        if not isinstance(shape, tuple):
            
            # Raises informative TypeError.
            raise TypeError("Shape argument is not a tuple.\n")
            
            
        # Checks if the elements in 'values' are of either int, float or bool.
        for element in values:
            
            if not isinstance(element, int):
                if not isinstance(element, float):
                    if not isinstance(element, bool):
                        
                        #Raises informative TypeError
                        raise TypeError("Argument contained value of type not allowed.\n")
        
        
        # Checks that there isn't a combination of types in 'values'.
        values_type = type(values[0])
        
        for element in values:
    
            if type(element) != values_type:
                
                # Raises informative ValueError.
                raise ValueError("Array-elements given as argument do not share the same type.\n")
    

        # Checks that the amount of values corresponds to the shape
        if shape[0] != len(values):
            
            # Raises informative ValueError
            raise ValueError("Amount of values given does not correspond to the shape.\n")


        # Sets instance attributes
        self.shape = shape
        self.values_list = []
        self.values_type = values_type
        
        for element in values:
            self.values_list.append(element)
            
            
            
    # This method returns the element at the given index of the array.
    def __getitem__(self, index):
        
        if isinstance(index, int):
            return self.values_list[index]
        else:
            
            # Raises informative TypeError.
            raise TypeError("Index argument should be of type int.\n")
        
        
        
    # Returns a string of the array in the form of [1, 2, 3, 4].
    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        
        result = "["
    
        for i in range(len(self.values_list)):
            
            """
            if self.values_type == float:
                formatted_string = format(self.values_list[i], '.2f')
                result += formatted_string + ", "
                
            else:
            """
            result += str(self.values_list[i]) + ", "
        
        result = result[:-2] # Removes the last ', '.
        result += "]"
        
        return result
        


    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        
        # Checks that the Array on the left side of the operator doesn't contain boolean values.
        if self.values_type == bool:
            return NotImplemented
        
        
        # Checks if the type of other doesn't match the type of the current Array.
        if type(other) != self.values_type:
            
            # Checks if other isn't an Array.
            if not isinstance(other, Array):
                return NotImplemented
            
            # If other is an array, checks if it isn't an array of the same type.
            elif self.values_type != other.values_type:
                 return NotImplemented
             
            # If other is an array of the same type, checks to see if the shapes do not match.
            elif other.shape != self.shape:
                
                # Raises informative ValueError
                raise ValueError("The shapes of the two Arrays do not match.\n")
                
        
        
        temp_list = []
        
        # Perform addition by scalar.
        if not isinstance(other, Array):
            
            for i in range(len(self.values_list)):
                
                temp_list.append(self.values_list[i] + other)
                
        # Performs addition by array.
        else:
            
            for i in range(len(self.values_list)):
                temp_list.append(self.values_list[i] + other.values_list[i])
        
        
        # Makes sure floating point numbers are rounded to a maximum of 2 decimals.
        if self.values_type == float:
            
            for i in range(len(temp_list)):
                temp_list[i] = round(temp_list[i], 2)
                
        
        # Returns the result as a new Array.
        return Array(self.shape, *temp_list)


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
            
        # Checks that the Array on the left side of the operator doesn't contain boolean values.
        if self.values_type == bool:
            return NotImplemented
        
        # Checks if the type of other doesn't match the type of the current Array.
        if type(other) != self.values_type:
            
            # Checks if other isn't an Array.
            if not isinstance(other, Array):
                return NotImplemented
            
            # If other is an array, checks if it isn't an array of the same type.
            elif self.values_type != other.values_type:
                 return NotImplemented
             
            # If other is an array of the same type, checks to see if the shapes do not match.
            elif other.shape != self.shape:
                
                # Raises informative ValueError
                raise ValueError("The shapes of the two Arrays do not match.\n")
        
        
        temp_list = []
        
        # Perform subtraction by scalar.
        if not isinstance(other, Array):
            
            for i in range(len(self.values_list)):
                
                temp_list.append(self.values_list[i] - other)
                
        # Performs subtraction by array.
        else:
            
            for i in range(len(self.values_list)):
                temp_list.append(self.values_list[i] - other.values_list[i])
        
        
        # Makes sure floating point numbers are rounded to a maximum of 2 decimals.
        if self.values_type == float:
            
            for i in range(len(temp_list)):
                temp_list[i] = round(temp_list[i], 2)
        
        
        # Returns the result as a new Array.
        return Array(self.shape, *temp_list)
        


    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        return self.__sub__(other)



    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        
        
        # Checks that the Array on the left side of the operator doesn't contain boolean values.
        if self.values_type == bool:
            return NotImplemented
        
        # Checks if the type of other doesn't match the type of the current Array.
        if type(other) != self.values_type:
            
            # Checks if other isn't an Array.
            if not isinstance(other, Array):
                return NotImplemented
            
            # If other is an array, checks if it isn't an array of the same type.
            elif self.values_type != other.values_type:
                 return NotImplemented
             
            # If other is an array of the same type, checks to see if the shapes do not match.
            elif other.shape != self.shape:
                
                # Raises informative ValueError
                raise ValueError("The shapes of the two Arrays do not match.\n")
        
        
        temp_list = []
        
        # Perform multiplication by scalar.
        if not isinstance(other, Array):
            
            for i in range(len(self.values_list)):
                
                temp_list.append(self.values_list[i] * other)
                
        # Performs multiplication by array.
        else:
            
            for i in range(len(self.values_list)):
                temp_list.append(self.values_list[i] * other.values_list[i])
        
        
        # Makes sure floating point numbers are rounded to a maximum of 2 decimals.
        if self.values_type == float:
            
            for i in range(len(temp_list)):
                temp_list[i] = round(temp_list[i], 2)
        
        
        # Returns the result as a new Array.
        return Array(self.shape, *temp_list)
        
        

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
    
        # Checks that 'other' is an Array, and if the shapes matches.
        if not isinstance(other, Array):
            return False
        
        elif other.shape != self.shape:
            return False
        
        # Checks each element in the arrays individually for inequality.
        for i in range(len(self.values_list)):
            
            if self.values_list[i] != other.values_list[i]:
                return False
            
        return True
    
    

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
            
                
        # Checks if the type of other doesn't match the type of the current Array.
        if type(other) != self.values_type:
            
            # Checks if other isn't an Array.
            if not isinstance(other, Array):
                raise TypeError("Other-argument given is not of a valid type.\n")
            
            # If other is an array, checks if it isn't an array of the same type.
            elif self.values_type != other.values_type:
                 raise TypeError("Other-argument given is not of a valid type.\n")
             
            # If other is an array of the same type, checks to see if the shapes do not match.
            elif other.shape != self.shape:
                
                # Raises informative ValueError
                raise ValueError("The shapes of the two Arrays do not match.\n")
        
            
        temp_list = []
        
        # Perform comparison by scalar.
        if not isinstance(other, Array):
            
            for i in range(len(self.values_list)):
                
                if self.values_list[i] == other:
                    temp_list.append(True)
                else:
                    temp_list.append(False)
                
        # Performs comparison by array.
        else:
            
            for i in range(len(self.values_list)):
                
                if self.values_list[i] == other.values_list[i]:
                    temp_list.append(True)
                else:
                    temp_list.append(False)
        
        
        # Returns the result as a new Array.
        return Array(self.shape, *temp_list)    
        


    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """

        if self.values_type == bool:
            raise TypeError("Array is of type boolean.\n")
        else:
            return float(min(self.values_list))



    def mean_element(self):
        """Returns the mean value of an array

        Only needs to work for type int and float (not boolean).

        Returns:
            float: the mean value
        """

        if self.values_type == bool:
            raise TypeError("Array is of type boolean.\n")
        else:
            result = float( sum(self.values_list) / len(self.values_list) )
            
            return round(result, 2)
