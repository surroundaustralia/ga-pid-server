import json
import pytest
import requests


def redirect(label, from_, headers=None):
    r = requests.get(from_, headers=headers, allow_redirects=False, timeout=2)
    return r.headers.get("location")


def create_cases(json_file):
    test_cases = []
    uris = json.load(open(json_file, "r"))
    for uri, cases in uris.items():
        for case in cases:
            test_cases.append((case["from"], case["to"],case["label"], case["headers"]))
    return test_cases


@pytest.mark.parametrize("test_input,expected,label,headers", create_cases("./testsPIDupgrade.data.json"))
def test_PID(test_input, expected, label, headers):
    assert redirect(label=label, from_=test_input, headers=headers) == expected

