#!/usr/bin/env python3
"""
This is a function that awaits and delay
"""
import asyncio
from typing import Type
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This is a function that awaits and delay
    """
    return asyncio.create_task(wait_random(max_delay))
