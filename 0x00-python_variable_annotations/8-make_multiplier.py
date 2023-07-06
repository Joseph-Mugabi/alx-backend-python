#!/usr/bin/env python3
"""
type-annotated function make_multiplier that takes a float
multiplier as argument, returns a function that multiplies
a float by multiplier.
"""
from typing import List, Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier."""
    return lambda any_float_num: multiplier * any_float_num
