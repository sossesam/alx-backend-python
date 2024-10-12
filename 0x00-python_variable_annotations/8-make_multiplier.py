#!/usr/bin/env python3
from typing import Callable
"""
Function:

Parameters-

Return-

Examples-


"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ function that returns a callable"""
    def func(n: float) -> float:
        return n * multiplier
    return func
