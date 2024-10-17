#!/usr/bin/env python3
"""
funtion for asyncio
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    funtion for asyncio
    """

    list_of_results = [wait_random(max_delay) for i in range(n)]

    result = await asyncio.gather(*list_of_results)

    return sorted(result)
