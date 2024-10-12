#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
'''
Function: element_length Parameters- lst Return-List of Tuple

Examples-
'''


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Iterable function '''

    i: int
    return [(i, len(i)) for i in lst]
