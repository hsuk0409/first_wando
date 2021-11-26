from json import dumps

import pytest

from web import app
from web.db.db_manager import DBManager
from web.tests.data.user_dummy_data import get_user_success_dummy_data

dbm = DBManager.get_instance()


@pytest.fixture
def api():
    test_api = app.app
    api = test_api.test_client()

    return api


def get_db_data(collection: str, where: dict) -> dict:
    return dbm.find_one(collection=collection, where=where)


def test_register_api(api):
    request_data = get_user_success_dummy_data()

    result = api.post("/user", json=request_data)
    assert result.status_code == 200

    where = {"alarmName": request_data.get("alarmName")}
    justin_data = get_db_data(collection="wando_test", where=where)

    assert justin_data is not None
    assert justin_data.get("alarmName") == request_data.get("alarmName")

    dbm.delete_many(collection="wando_test", where={"_id": justin_data.get("_id")})
    justin_data = get_db_data(collection="wando_test", where=where)

    assert justin_data is None
