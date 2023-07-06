#!/usr/bin/env python3
"""
The types of the elements of the input are not know
"""
from typing import List, Sequence, Union, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """ Returns first elemnts of the list or None"""
    if lst:
        return lst[0]
    else:
        return None
