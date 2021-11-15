from functools import wraps

import pymongo

from pymongo import database, MongoClient, errors


def db_transaction(mongo_func):
    @wraps(mongo_func)
    def wrapper(*args, **kwargs):
        args[0].connect()
        return mongo_func(*args, **kwargs)

    return wrapper


class DBMongo(object):

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.my_db: pymongo.database.Database = None
        self.client: MongoClient = None

    def connect(self):
        if not self.client:
            try:
                self.client = MongoClient()
            except pymongo.errors.ServerSelectionTimeoutError as er:
                print(str(er))  # TODO 로깅으로 변경
            self.my_db = self.client[self.db_name]

    def close(self):
        if self.client:
            self.client.close()
