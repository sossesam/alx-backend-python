#!/usr/bin/env python3
"""
0. Async Generator
"""
import asyncio
import random
from typing import async_generator

async def async_generator() -> async_generator[float]:
    """
    0. Async Generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
