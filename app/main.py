from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from huey import RedisHuey
from pathlib import Path

app = FastAPI()

huey = RedisHuey(url='redis://localhost:6379/0')

app.mount("/static", StaticFiles(directory="templates"), name="static")

@huey.task()
def set_key_value(key: str, value: str):
    key_value_store[key] = value

key_value_store = {}

@app.get("/", response_class=HTMLResponse)
def read_root():
    return FileResponse("templates/index.html")

@app.get("/get/{key}")
def read_item(key: str):
    value = key_value_store.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"key": key, "value": value}

@app.post("/set/{key}/{value}")
async def set_item(key: str, value: str):
    set_key_value.schedule(args=(key, value), delay=0)
    return {"message": "Task enqueued for setting key-value pair."}
