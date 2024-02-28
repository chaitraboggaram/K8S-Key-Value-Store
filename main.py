from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

app.mount("/static", StaticFiles(directory="templates"), name="static")

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
def set_item(key: str, value: str):
    key_value_store[key] = value
    return {"key": key, "value": value}
