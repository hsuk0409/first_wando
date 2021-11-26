from json import dumps

import pytest

from web import app
from web.db.db_manager import DBManager
from web.tests.data.user_dummy_data import get_user_success_dummy_data


@pytest.fixture
def api():
    test_api = app.app
    api = test_api.test_client()

    return api


def test_register_api(api):
    request_data = get_user_success_dummy_data()

    result = api.post("/user", json=request_data)
    assert result.status_code == 200

    dbm = DBManager.get_instance()
    justin_data = dbm.find_one(collection="wando_test", where={"alarmName": request_data.get("alarmName")})

    assert justin_data.get("alarmName") == request_data.get("alarmName")
