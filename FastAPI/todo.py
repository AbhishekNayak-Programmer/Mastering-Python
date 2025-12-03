from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from bson import ObjectId
import motor.motor_asyncio

app = FastAPI()

# ---------------------------
#   DATABASE CONNECTION
# ---------------------------
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client["abhishek_nayak"]  # your DB name
todo_collection = db["todos"]  # collection name


# ------------------------------------
#   Allow Frontend for CRUD Operation
# -------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Allow all frontends (or replace with specific domains)
    allow_credentials=True,
    allow_methods=["*"],   # GET, POST, PUT, DELETE, OPTIONS...
    allow_headers=["*"],   # Authorization, Content-Type...
)

# ---------------------------
#   Pydantic Models
# ---------------------------
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoResponse(TodoBase):
    id: str


# ---------------------------
#   Helper Function
# ---------------------------
def todo_helper(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo.get("description"),
        "completed": todo["completed"],
    }


# ---------------------------
#   ROUTES (CRUD)
# ---------------------------

# CREATE
@app.post("/todos", response_model=TodoResponse)
async def create_todo(todo: TodoBase):
    new_todo = await todo_collection.insert_one(todo.dict())
    created = await todo_collection.find_one({"_id": new_todo.inserted_id})
    return todo_helper(created)


# READ ALL
@app.get("/todos", response_model=List[TodoResponse])
async def get_todos():
    todos = []
    async for todo in todo_collection.find():
        todos.append(todo_helper(todo))
    return todos


# READ ONE
@app.get("/todos/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: str):
    todo = await todo_collection.find_one({"_id": ObjectId(todo_id)})
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo_helper(todo)


# UPDATE
@app.put("/todos/{todo_id}", response_model=TodoResponse)
async def update_todo(todo_id: str, data: TodoBase):
    update_result = await todo_collection.update_one(
        {"_id": ObjectId(todo_id)},
        {"$set": data.dict()}
    )

    if update_result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")

    updated = await todo_collection.find_one({"_id": ObjectId(todo_id)})
    return todo_helper(updated)


# DELETE
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str):
    result = await todo_collection.delete_one({"_id": ObjectId(todo_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
