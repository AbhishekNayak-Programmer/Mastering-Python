# Command to run this : fastapi dev main.py --port 4040
from fastapi import FastAPI, HTTPException
from typing import List, Optional
from enum import IntEnum
from pydantic import BaseModel, Field

api = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MED = 2
    HIGH = 3

class TodoBase(BaseModel):
    todo_name : str = Field(..., min_length=3, max_length=512, description="Name of the todo")
    todo_desc : str = Field(..., description="description of the todo")
    priority : Priority = Field(default=Priority.LOW, description="priority of the todo")

class TodoCreate(TodoBase):
    pass 

class Todo(TodoBase):
    todo_id : int = Field(..., description="Unique identifier of the todo")

class TodoUpdate(BaseModel):
    todo_name : Optional[str] = Field(None, min_length=3, max_length=512, description="Name of the todo")
    todo_desc : Optional[str] = Field(None, description="description of the todo")
    priority : Optional[Priority] = Field(None, description="priority of the todo") 


all_todos = [
    Todo(todo_id=1, todo_name="sports", todo_desc="play some games", priority=Priority.LOW),
    Todo(todo_id=2, todo_name="study", todo_desc="study for sometimes", priority=Priority.MED),
    Todo(todo_id=3, todo_name="read", todo_desc="read a book", priority=Priority.MED),
    Todo(todo_id=4, todo_name="play", todo_desc="play a game", priority=Priority.LOW),
    Todo(todo_id=5, todo_name="eat", todo_desc="eating => breakfast, lunch & dinner", priority=Priority.HIGH),
]

# GET, POST, PUT, DELETE
# @api.get("/")
# def index():
#     return {"message": "Hello world"}

# You have to mention the int value as that will be treated as a string if you dont mention
@api.get("/todos/{todo_id}", response_model=Todo)
def getTodo(todo_id:int):
    for todo in all_todos:
        if todo.todo_id == todo_id :
            return todo 
    raise HTTPException(status_code=404, detail="Error, Todo not found with id")


# localhost:8000/todos?first_n=3 when we will return only last 3 
# localhost:8000/todos is default when we will return all todos
@api.get("/todos", response_model=List[Todo])
def allTodos(first_n:int = None):
    if first_n :
        return all_todos[:first_n]
    else:
        return all_todos
    
@api.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max(todo.todo_id for todo in all_todos) + 1
    new_todo = Todo(
        todo_id = new_todo_id,
        todo_name = todo.todo_name,
        todo_desc = todo.todo_desc,
        priority = todo.priority
    )
    all_todos.append(new_todo)
    return new_todo


@api.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, _todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id :
            if _todo.todo_name is not None:
                todo.todo_name = _todo.todo_name
            if _todo.todo_desc is not None:
                todo.todo_desc = _todo.todo_desc
            if _todo.todo_priorityname is not None:
                todo.priority = _todo.priority
            return todo
    raise HTTPException(status_code=404, detail="Error, Todo not found with id")


@api.delete('/todos/{todo_id}')
def update_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id :
            deleted_todo = all_todos.pop(index)
            return {"message" : f"Todo with id {todo_id} deleted!", "todo_data": deleted_todo}
    raise HTTPException(status_code=404, detail="Error, Todo not found with id")