from huey import RedisHuey
import redis

redis_pool = redis.ConnectionPool.from_url("redis://redis:6379/0")
redis_client = redis.StrictRedis(connection_pool=redis_pool)
huey = RedisHuey('entrypoint', host='redis')

@huey.task()
def set_key_value(key: str, value: str):
    print(f"Setting key: {key}, value: {value}")
    redis_client.set(key, value)
