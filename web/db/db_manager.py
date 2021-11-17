from web.db.db_mongo import DBMongo


class DBManager(DBMongo):
    _instance = None

    def __init__(self):
        super().__init__(db_name="admin")

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance
