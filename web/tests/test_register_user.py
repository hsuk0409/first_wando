import json

import pytest

from web import app


@pytest.fixture
def api():
    test_api = app.app
    api = test_api.test_client()

    return api


def test_get_response_dict(api):
    result = api.post("/user")
    print(result)
    data = json.loads(result.data.decode('utf-8'))
    print(data)
    assert type(data) == dict
