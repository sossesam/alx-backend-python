#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay : int=10) -> float:
    random_num = random.random() * max_delay
    result = await asyncio.sleep(random_num)
    return random_num