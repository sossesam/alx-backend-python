#!/usr/bin/env python3
"""
funtion for asyncio
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    funtion for asyncio
    """

    list_of_results = [task_wait_random(max_delay) for i in range(n)]

    result = await asyncio.gather(*list_of_results)

    return sorted(result)
