#!/usr/bin/env python3
import math


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
