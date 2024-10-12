#!/usr/bin/env python3
import math
"""
Description: A function that coverts a float to an int

parameters- It takes a float as an argument

return- returns a floored integer
"""


def floor(n: float) -> int:
    """
    Return the largest integer less than or equal to n.

    Parameters:
        n (float): The number to be floored.

    Returns:
        int: The floored integer value.

    Examples:
        >>> floor(3.7)
        3
        >>> floor(-2.3)
        -3
    """
    return math.floor(float(n))
