#!/usr/bin/env python3

"""
Module tests GithubOrgClient methods
"""

from unittest import TestCase, mock
from unittest.mock import patch, Mock, PropertyMock, call
from typing import Dict
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(TestCase):
    """
    Class tests GithubOrgClient methods
    """

    @parameterized.expand(
        [
            ("google", {"tydd": "xyrt"}),
            ("abc", {"name": "Abc"}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org: str, expected: Dict, mock_org: Mock):
        """Tests org method"""
        mock_org.return_value = expected
        objct = GithubOrgClient(org)
        self.assertEqual(objct.org, expected)
        mock_org.assert_called_once_with("https://api.github.com/orgs/" + org)

    def test_public_repos_url(self):
        """Method tests _public_repos_url"""
        expected = "https://api.github.com/orgs/repo"
        payload = {"repos_url": "https://api.github.com/orgs/repo"}
        with patch('client.GithubOrgClient.org', PropertyMock(
                    return_value=payload)):
            objct = GithubOrgClient("TechAccess")
            self.assertEqual(objct._public_repos_url, expected)

    @patch("client.get_json")
    def test_public_repos(self, mock_objct: Mock):
        """Method tests property _public_repos"""
        expected = {"Command": "git_push"}
        mock_objct.return_value = expected

        result = "github.com/techaccess"
        with patch("client.GithubOrgClient._public_repos_url", PropertyMock(
                    return_value=result)) as mock_repo:
            obj = GithubOrgClient("TechAccess")
            self.assertEqual(obj._public_repos_url, result)

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False)
        ]
    )
    def test_has_license(self, repo: Dict[str, Dict],
                         license_key: str, expected: bool):
        """tests license"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(TestCase):
    """Implement intergration test for public_repos method"""

    @classmethod
    def setUpClass(cls):
        """Prepare to test"""
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        org_mock = Mock()
        org_mock.json = Mock(return_value=org)
        cls.org_mock = org_mock
        repos_mock = Mock()
        repos_mock.json = Mock(return_value=repos)
        cls.repos_mock = repos_mock

        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()
        options = {cls.org_payload["repos_url"]: repos_mock}
        cls.get.side_effect = lambda y: options.get(y, org_mock)

    @classmethod
    def tearDownClass(cls):
        """ unprepare for testing """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ public repos test """
        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])

    def test_public_repos_with_license(self):
        """ public repos test """
        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.assertEqual(y.public_repos("apache-2.0"), self.apache2_repos)
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])
