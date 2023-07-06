#!/usr/bin/env python3
"""
type-annotated function sum_mixed_list which takes a list mxd_lst of integers
floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """returns their sum as a float."""
    return float(sum(mxd_lst))
