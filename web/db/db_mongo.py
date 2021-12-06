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
                # self.client = MongoClient(settings.MONGO_ADDRESS,
                #                           port=int(settings.MONGO_PORT),
                #                           username=settings.MONGO_USERNAME,
                #                           password=settings.MONGO_PASSWORD,
                #                           serverSelectionTimeoutMS=10000)
                self.client = MongoClient(host='localhost', port=27017)
            except pymongo.errors.ServerSelectionTimeoutError as er:
                print(str(er))  # TODO 로깅으로 변경
            self.my_db = self.client[self.db_name]

    def close(self):
        if self.client:
            self.client.close()

    @db_transaction
    def find_one(self, collection: str, where: dict = None, projection: dict = None) -> dict:
        document = self.my_db[collection].find_one(filter=where, projection=projection)
        if not document:
            print(f"No DB data in {collection} where {where}")
        return document

    @db_transaction
    def insert_one(self, collection: str, document: dict):
        result = self.my_db[collection].insert_one(document=document).inserted_id
        return result

    @db_transaction
    def delete_many(self, collection: str, where: dict = None):
        result = self.my_db[collection].delete_many(where)
        if result.deleted_count < 1:
            print(f"Delete Count < 1")
        return result
