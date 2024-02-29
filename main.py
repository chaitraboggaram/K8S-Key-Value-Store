from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from huey import RedisHuey
import redis

app = FastAPI()

huey = RedisHuey(url='redis://localhost:6379/0')

# Initialize Redis client on startup
redis_pool = redis.ConnectionPool.from_url("redis://localhost:6379/0")
redis_client = redis.StrictRedis(connection_pool=redis_pool)

app.mount("/templates", StaticFiles(directory="templates"), name="templates")

@huey.task()
def set_key_value(key: str, value: str):
    print(f"Setting key: {key}, value: {value}")
    redis_client.set(key, value)

@app.on_event("startup")
def startup_event():
    # Add any other startup tasks if needed
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
