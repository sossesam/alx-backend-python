#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable) -> List[Tuple[Sequence, int]]:
    i: int
    return [(i, len(i)) for i in lst]