import configparser
import os
from pymongo import MongoClient

from src.consumer import QueryHandler


class MongoDB:
    client = None
    db = None

    @staticmethod
    def initialize(create=False):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), '../../ressource/config/config.ini'))

        MongoDB.client = MongoClient(config.get("DATABASE", "URI"), config.getint("DATABASE", "PORT"))

        if create:
            MongoDB.createDatabase(config.get("DATABASE", "DB_NAME"))


    @staticmethod
    def disconnect():
        QueryHandler.queryAll()
        MongoDB.client.close()


    @staticmethod
    def createDatabase(dbName):
        if MongoDB.db is None:
            MongoDB.dropDatabase(dbName)

        MongoDB.db = MongoDB.client[dbName]

    @staticmethod
    def dropDatabase(dbName):
        if MongoDB.client is not None:
            MongoDB.client.drop_database(dbName)

    @staticmethod
    def insert(collName, data):
        MongoDB.db[collName].insert_one(data)

    @staticmethod
    def insertMany(collName, data):
        MongoDB.db[collName].insert_many(data)

    @staticmethod
    def updateMany(collName, data):
        MongoDB.db[collName].update_many({}, data)
