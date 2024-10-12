#!/usr/bin/env python3
from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: List = [12, 72, 91]

zoom_2xL: Tuple = zoom_array(array)