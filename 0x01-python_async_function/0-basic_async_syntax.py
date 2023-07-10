#!/usr/bin/env python3
"""
asyncio
"""
import random 
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ returns an integer after a delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
