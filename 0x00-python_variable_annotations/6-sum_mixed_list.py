#!/usr/bin/env python3
"""
funtion for asyncio
"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:

    n: float = 0
    x: float
    for x in mxd_lst:
        n = n + x

    return n
