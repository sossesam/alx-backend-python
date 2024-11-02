#!/usr/bin/env python3
"""
funtion for asyncio
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    funtion for asyncio
    """
    zoomed_in: Tuple = (
        item for item in lst
        for i in range(factor)
    )
    return list(zoomed_in)


array: Tuple = (12, 72, 91)

zoom_2xL: Tuple = zoom_array(array)

zoom_3x: Tuple= zoom_array(array, 3)