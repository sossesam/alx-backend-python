#!/usr/bin/env python3

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import List

async def wait_n(n: int, max_delay: int) -> List[float]:
    list_of_results: List = [wait_random(max_delay) for i in range(n)]
    
    result: List = await asyncio.gather(*list_of_results)

    return sorted(result)

    
    
        



    
        
