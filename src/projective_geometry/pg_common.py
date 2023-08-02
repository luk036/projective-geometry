"""
This module contains functions that are common to projective plane.
"""

# Write a dot product of two vectors.
def dot_product(vector1, vector2):
    """
    The dot_product function calculates the dot product of two vectors.
    
    :param vector1: The first vector, represented as a list of numbers
    :param vector2: The `vector1` and `vector2` parameters are lists representing two vectors. Each
    element in the list corresponds to a component of the vector. For example, if `vector1 = [1, 2, 3]`
    and `vector2 = [4, 5,
    :return: The dot product of the two vectors.

    :Example:
    >>> dot_product([1, 2, 3], [4, 5, 6])
    32
    >>> dot_product([1, 2, 3], [4, 5, 6, 7])
    Traceback (most recent call last):
    ...
    ValueError: Vectors must be the same length
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be the same length")
    return sum(vector1[i] * vector2[i] for i in range(len(vector1)))

# Write a cross product of two vectors.
def cross_product(vector1, vector2):
    """
    The function `cross_product` calculates the cross product of two 3D vectors.
    
    :param vector1: The first vector, represented as a list of three numbers [x1, y1, z1]
    :param vector2: The above code defines a function `cross_product` that takes two vectors as input
    and returns their cross product. The vectors must be 3-dimensional and have the same length
    :return: a list containing the components of the cross product of the two input vectors.

    :Example:
    >>> cross_product([1, 2, 3], [4, 5, 6])
    [-3, 6, -3]
    >>> cross_product([1, 2, 3], [4, 5, 6, 7])
    Traceback (most recent call last):
    ...
    ValueError: Vectors must be the same length
    >>> cross_product([1, 2, 3], [4, 5])
    Traceback (most recent call last):
    ...
    ValueError: Vectors must be the same length
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be the same length")
    if len(vector1) != 3:
        raise ValueError("Vectors must be 3D")
    return [
        vector1[1] * vector2[2] - vector1[2] * vector2[1],
        vector1[2] * vector2[0] - vector1[0] * vector2[2],
        vector1[0] * vector2[1] - vector1[1] * vector2[0]
    ]
