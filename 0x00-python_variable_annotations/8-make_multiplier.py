#!/usr/bin/env python3
"""
funtion for asyncio
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ function that returns a callable"""
    def func(n: float) -> float:
        return n * multiplier
    return func
