"""Unit and security tests for recursive_json_search.json_search."""

import unittest

from recursive_json_search import json_search
from test_data import data, key1, key2


class json_search_test(unittest.TestCase):
    """Validate recursive search behavior and the access-control policy."""

    def test_search_found(self):
        """A nested key should produce a non-empty result for an allowed role."""
        self.assertNotEqual([], json_search(key1, data, role="viewer"))

    def test_search_not_found(self):
        """An absent key should produce an empty list."""
        self.assertEqual([], json_search(key2, data, role="viewer"))

    def test_is_a_list(self):
        """The function should always return a list."""
        self.assertIsInstance(json_search(key1, data, role="viewer"), list)

    def test_admin_can_read_api_key(self):
        """An admin should be able to read the protected API key."""
        result = json_search("apiKey", data, role="admin")
        self.assertEqual([{"apiKey": "SNMP-COMMUNITY-STRING-7f3a9c"}], result)

    def test_viewer_cannot_read_api_key(self):
        """A viewer must not receive the protected API key."""
        self.assertEqual([], json_search("apiKey", data, role="viewer"))

    def test_operator_can_read_management_ip(self):
        """An operator should be able to read a management IP address."""
        result = json_search("managementIpAddress", data, role="operator")
        self.assertEqual([{"managementIpAddress": "10.10.20.21"}], result)

    def test_viewer_cannot_read_management_ip(self):
        """A viewer must not receive a management IP address."""
        self.assertEqual(
            [], json_search("managementIpAddress", data, role="viewer")
        )

    def test_missing_role_is_denied_for_protected_key(self):
        """A protected key request without a role must fail closed."""
        self.assertEqual([], json_search("apiKey", data))


if __name__ == "__main__":
    unittest.main()
