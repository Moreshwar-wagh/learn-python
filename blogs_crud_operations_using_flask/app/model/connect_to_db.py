from pymongo import MongoClient
from app import app


class ConnectDB:

    def __init__(self):
        self.connection = None
        self.collection = None

    def connect_db(self, db='', collection=''):
        connection = MongoClient(host="localhost")

        self.connection = connection[app.db]
        return self.connection
