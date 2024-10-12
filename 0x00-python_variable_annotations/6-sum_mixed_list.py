#!/usr/bin/env python3
from typing import List, Union
"""
Function:

Parameters-

Return-

Examples-


"""

def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:

    n: float = 0
    x: float
    for x in mxd_lst:
        n = n + x

    return n
