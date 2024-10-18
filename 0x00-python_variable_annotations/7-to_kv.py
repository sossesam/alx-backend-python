#!/usr/bin/env python3
"""
funtion for asyncio
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    funtion for asyncio
    """

    return (k, v**2)
