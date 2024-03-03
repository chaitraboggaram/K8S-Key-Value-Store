import os
from huey import RedisHuey
import redis

REDIS_HOST = os.environ.get("REDIS_HOST", "redis-primary-service") or 'localhost' or '127.0.0.1'
redis_pool = redis.ConnectionPool.from_url(f"redis://{REDIS_HOST}:6379/0")
redis_client = redis.StrictRedis(connection_pool=redis_pool)
huey = RedisHuey('entrypoint', host=REDIS_HOST)

@huey.task()
def set_key_value(key: str, value: str):
    print(f"Setting key: {key}, value: {value}")
    redis_client.set(key, value)
