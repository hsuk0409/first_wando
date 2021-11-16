import pytest
from pymongo import MongoClient


@pytest.fixture
def mongo():
    host = "localhost"
    port = "27017"

    mongo = MongoClient(host, int(port))

    return mongo


def test_connect_mongodb(mongo):
    print(mongo)
    assert mongo is not None


def test_register_simple_user(mongo):
    result = mongo["local_test"]["wando_test"].insert_one({"name": "justin", "age": 28}).inserted_id

    print(result)

