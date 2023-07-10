#!/usr/bin/env python
"""
async function
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns a list of all delays"""
    n_tasks = []
    n_delays = []
    for j in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        n_tasks.append(task)
    for task in asyncio.as_completed(n_tasks):
        n_delays.append(await task)
    return n_delays
