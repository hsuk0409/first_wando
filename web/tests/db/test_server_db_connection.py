from web.db.db_manager import DBManager


def test_connect_server_db():
    dbm = DBManager.get_instance()
    result = dbm.find_one(collection="wando_test")

    assert result is None
