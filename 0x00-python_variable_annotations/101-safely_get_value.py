#!/usr/bin/env python3
"""return values, add type annotations to the function"""
from typing import List, Union, Any, Mapping, TypeVar
t = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[t, None] = None) -> Union[Any, t]:
    """ Returns first element in a dictionary """
    if key in dct:
        return dct[key]
    else:
        return default
