#!/usr/bin/env python3
"""
1. Async Comprehensions
"""
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    1. Async Comprehensions
    """
    result = [i async for i in async_generator()]
    return result
