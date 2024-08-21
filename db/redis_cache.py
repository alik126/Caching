import redis
import json
from bson import ObjectId
from config import REDIS_HOST, REDIS_PORT, REDIS_DB

cache = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)


def json_serializer(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError(f"Type {type(obj)} not serializable")


def cache_user(user_data):
    cache.setex(user_data['username'], 3600, json.dumps(user_data, default=json_serializer))


def get_user_from_cache(username):
    user_data = cache.get(username)
    return json.loads(user_data) if user_data else None
