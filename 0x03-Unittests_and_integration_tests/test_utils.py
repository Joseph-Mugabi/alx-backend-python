#!/usr/bin/env python3
"""
module implements unittests
"""
from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from typing import Dict, Union, Tuple
from utils import access_nested_map, get_json, memoize


class TechAccessNestedMap(TestCase):
    """implementing unittest class for TestAccessNestedMap"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple, expected: Union[int, str]):
        """test access_nested map func"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
