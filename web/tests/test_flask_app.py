import pytest

from web import app


@pytest.fixture
def api():
    test_api = app.app
    api = test_api.test_client()

    return api


def test_init_app(api):
    response = api.get("/")

    result_str = str(response.data, "utf-8")
    assert result_str == "hello, wando!"

