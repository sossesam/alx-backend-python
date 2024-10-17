#!/usr/bin/env python3
"""
This is a function that awaits and delay
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This is a function that awaits and delay
    """

    random_num = random.random() * max_delay
    result = await asyncio.sleep(random_num)
    return random_num
