#!/usr/bin/env python3
"""
returns a tuple
"""

from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple"""
    return (k, float(v ** 2))
