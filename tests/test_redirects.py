import json
import pytest
import httpx


def redirect(label, from_, headers=None):
    r = httpx.get(from_, headers=headers, follow_redirects=False, timeout=2)
    return r.headers.get("location")


def create_cases(json_file, host="http://pid.geoscience.gov.au"):
    test_cases = []
    uris = json.load(open(json_file, "r"))
    for uri, cases in uris.items():
        for case in cases:
            test_cases.append((case["from"].replace("{HOST}", host), case["to"], case["label"], case["headers"]))
    return test_cases


@pytest.mark.parametrize("test_input,expected,label,headers", create_cases("/usr/local/PID_tests/rule-cases.json"))
def test_pid(test_input, expected, label, headers):
    assert redirect(label=label, from_=test_input, headers=headers) == expected, label
