#!/usr/bin/env python3

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import List

async def wait_n(n: int, max_delay: int) -> List:
    list_of_results = [wait_random(max_delay) for i in range(n)]
    
    result = await asyncio.gather(*list_of_results)

    return sorted(result)

    
    
        



    
        
