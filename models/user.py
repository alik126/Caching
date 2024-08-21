from bson import ObjectId
from db.mongodb import get_user_from_db, users_collection
from db.redis_cache import cache_user, get_user_from_cache


def convert_objectId_to_str(user_data):
    if '_id' in user_data and isinstance(user_data['_id'], ObjectId):
        user_data['_id'] = str(user_data['_id'])
    return user_data


def add_user(username, email, age):
    user_data = {
        'username': username,
        'email': email,
        'age': age
    }
    user_id = users_collection.insert_one(user_data).inserted_id
    user_data['_id'] = user_id
    cache_user(convert_objectId_to_str(user_data))
    return user_id



def get_user(username):
    user = get_user_from_cache(username)
    if user:
        print("User data fetched from Redis cache")
        return user

    user = get_user_from_db(username)
    if user:
        print("User data fetched from MongoDB")
        cache_user(user)

    return user
