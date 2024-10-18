#!/usr/bin/env python3
"""
funtion for asyncio
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    # returns the sum of all argument in the list

    n: float = 0
    x: float
    for x in input_list:
        n = n + x

    return n
