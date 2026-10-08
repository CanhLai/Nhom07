"""Recursive JSON search with role-based access control."""

from policy import POLICY
from test_data import data


def json_search(key, input_object, role=None):
    """Return all ``{key: value}`` matches visible to ``role``.

    Keys listed in ``POLICY`` are protected. Access is denied by default when
    the role is missing, unknown, or not explicitly allowed for the key.
    """
    if key in POLICY and role not in POLICY[key]:
        return []

    results = []

    if isinstance(input_object, dict):
        for current_key, value in input_object.items():
            if current_key == key:
                results.append({current_key: value})
            if isinstance(value, (dict, list)):
                results.extend(json_search(key, value, role))
    elif isinstance(input_object, list):
        for item in input_object:
            if isinstance(item, (dict, list)):
                results.extend(json_search(key, item, role))

    return results


if __name__ == "__main__":
    print(json_search("issueSummary", data, role="viewer"))
