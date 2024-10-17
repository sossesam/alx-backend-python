#!/usr/bin/env python3
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

"""
funtion for asyncio
"""


def measure_time(n: int, max_delay: int) -> float:
    """
    funtion for asyncio
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start)/n
