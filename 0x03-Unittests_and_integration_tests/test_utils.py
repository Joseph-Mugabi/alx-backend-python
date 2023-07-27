#!/usr/bin/env python3
"""
module implements unittests
"""
from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from typing import Dict, Union, Tuple
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """implementing unittest class for TestAccessNestedMap"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple, expected: Union[int, str]):
        """test access_nested map func"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple):
        """tests raise of key error exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
