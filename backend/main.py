from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import *

# App object
app = FastAPI()

# CORS handle
origins = ["https://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    res = {
        "Ping": "Pong",
        "Hello": "world"
    }
    return res

@app.get("/api/todo")
async def get_todo():
    res = await get_all()
    return res

@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_id(title):
    res = await get_one(title)
    if (res):
        return res
    raise HTTPException(404, f"There is no no todo item like: {title}")

@app.post("/api/todo", response_model=Todo)
async def create_todo(todo:Todo):
    res = await create(dict(todo))
    if (res):
        return res
    raise HTTPException(400, "Something went wrong")

@app.put("/api/todo/{title}", response_model=Todo)
async def update_todo(title:str, desc:str):
    res = await update(title, desc)
    if (res):
        return res
    raise HTTPException(404, f"There is no no todo item like: {title}")

@app.delete("/api/todo/{title}")
async def delete_todo(title):
    res = await delete(title)
    if (res):
        return res
    raise HTTPException(404, f"There is no no todo item like: {title}")