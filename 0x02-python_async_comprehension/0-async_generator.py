#!/usr/bin/env python3
"""
0. Async Generator
"""
import asyncio
import random


async def async_generator():
    """
    0. Async Generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
