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


class TestGetJson(TestCase):
    """implementing testgetjson class that inherits from utils"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url: str, expected: Dict):
        """method test get json"""
        mock_get = Mock()
        mock_get.json.return_value = expected

        with patch("requests.get", return_value=mock_get) as mock_request:
            output_result = get_json(test_url)
            self.assertEqual(output_result, expected)
            mock_request.assert_called_once()


class TestMemoize(TestCase):
    """class tests memoize func"""

    def test_memoize(self):
        """tests memoize func"""
        class TestClass:
            """test class"""
            def a_method(self):
                """returns value 42"""
                return 42

            @memoize
            def a_property(self):
                """returns memoize property"""
                return self.a_method()

        with patch.object(TestClass, "a_method",
                          return_value=42) as mock_method:
            testclass = TestClass()
            output_result = testclass.a_property
            output_result = testclass.a_property
            self.assertEqual(output_result, 42)
            mock_method.assert_called_once()
