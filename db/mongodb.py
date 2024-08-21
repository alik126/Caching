from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["lab"]
users_collection = db["users"]


def insert_user(user_data):
    result = users_collection.insert_one(user_data)
    return result.inserted_id


def get_user_from_db(username):
    return users_collection.find_one({"username": username})
