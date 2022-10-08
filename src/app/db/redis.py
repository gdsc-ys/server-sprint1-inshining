import json
import redis

pool = redis.Redis(host="localhost", port="6379")

def get_redis_obj(key : str):
    result = pool.get(key)
    if result is None:
        return result
    return json.loads(result.decode("utf-8"))

def write_redis_obj(key, value):
    json_board = json.dumps(value,ensure_ascii=False).encode("utf-8")
    is_success = pool.set(key, json_board)
    return is_success