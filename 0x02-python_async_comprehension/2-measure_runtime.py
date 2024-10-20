#!/usr/bin/env python3
"""
2. Run time for four parallel comprehensions
mandatory
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    2. Run time for four parallel comprehensions
    mandatory
    """
    start = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(), async_comprehension(),
                         async_comprehension())
    end = time.time()

    return end - start
