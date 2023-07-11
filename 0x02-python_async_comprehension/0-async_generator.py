#!/usr/bin/env python3
"""
yield a random number between 0 and 10.
"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """ yield a random number btn 0 and q0 asynchronously """
    for j in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
