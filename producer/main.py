import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from huey import RedisHuey
import redis

app = FastAPI()

REDIS_HOST = os.environ.get("REDIS_HOST", "redis-primary-service") or 'localhost' or '127.0.0.1'
redis_pool = redis.ConnectionPool.from_url(f"redis://{REDIS_HOST}:6379/0")
redis_client = redis.StrictRedis(connection_pool=redis_pool)
huey = RedisHuey('entrypoint', host=REDIS_HOST)

@huey.task()
def set_key_value(key: str, value: str):
    print(f"Setting key: {key}, value: {value}")
    redis_client.set(key, value)

@huey.task()
def update_key_value(key: str, value: str):
    print(f"Updating key: {key}")
    redis_client.set(key, value)

@huey.task()
def delete_key(key: str):
    print(f"Deleting key: {key}")
    redis_client.delete(key)

@app.on_event("startup")
def startup_event():
    pass

@app.get("/", response_class=HTMLResponse)
def read_root():
    return FileResponse("templates/index.html")

@app.get("/get/{key}")
def read_item(key: str):
    value = redis_client.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"key": key, "value": value.decode()}

@app.post("/set/{key}/{value}")
async def set_item(key: str, value: str):
    set_key_value.schedule(args=(key, value), delay=0)
    return {"message": "Task enqueued for setting key-value pair."}

@app.put("/update/{key}/{value}")
async def update_item(key: str, value: str):
    if not redis_client.exists(key):
        raise HTTPException(status_code=404, detail="Key not found")
    update_key_value.schedule(args=(key, value), delay=0)
    return {"message": "Task enqueued for updating key-value pair."}

@app.delete("/delete/{key}")
async def delete_item(key: str):
    if not redis_client.exists(key):
        raise HTTPException(status_code=404, detail="Key not found")
    delete_key.schedule(args=(key,), delay=0)
    return {"message": "Task enqueued for setting key-value pair."}