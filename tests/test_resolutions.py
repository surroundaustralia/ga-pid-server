import json
import pytest
import httpx


def redirect(label, from_, headers=None):
    r = httpx.get(from_, headers=headers, follow_redirects=True, timeout=2)
    return r.status_code


def create_cases(json_file, host="http://localhost:80"):
    test_cases = []
    uris = json.load(open(json_file, "r"))
    for uri, cases in uris.items():
        for case in cases:
            test_cases.append((case["from"].replace("{HOST}", host), case["to"], case["label"], case["headers"]))
    return test_cases


@pytest.mark.parametrize("test_input,expected,label,headers", create_cases("rule-cases.json"))
def test_pid(test_input, expected, label, headers):
    assert redirect(label=label, from_=test_input, headers=headers) == 200


@pytest.mark.parametrize("test_input,expected,label,headers", create_cases("extra-rule-cases.json"))
def test_extra_pid(test_input, expected, label, headers):
    assert redirect(label=label, from_=test_input, headers=headers) == 200