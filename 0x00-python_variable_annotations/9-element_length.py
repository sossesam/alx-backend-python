#!/usr/bin/env python3
"""
Function:

Parameters-

Return-

Examples-


"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    i: int
    return [(i, len(i)) for i in lst]
