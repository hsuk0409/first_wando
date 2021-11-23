import json

import pytest

from web import app
from web.tests.data.user_dummy_data import get_user_fail_empty_day_of_week


@pytest.fixture
def api():
    test_api = app.app
    api = test_api.test_client()

    return api


def test_init_app(api):
    response = api.get("/")

    result_str = str(response.data, "utf-8")
    assert result_str == "hello, wando!"


def test_get_response_dict(api):
    result = api.post("/user")
    data = result.json
    assert type(data) == dict


def test_register_user_fail(api):
    request_data = get_user_fail_empty_day_of_week()
    response = api.post("/user", json=request_data)

    assert response.status_code == 200

    json_res = response.json
    result = json_res.get("result")
    assert result.get("return_code") == 401
    assert result.get("message")
