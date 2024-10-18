#!/usr/bin/env python3
"""
funtion for asyncio
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Iterable function '''

    i: int
    return [(i, len(i)) for i in lst]
