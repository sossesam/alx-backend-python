#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
'''
Function:

Parameters-

Return-

Examples-


'''


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Iterable function '''
    i: int
    return [(i, len(i)) for i in lst]
