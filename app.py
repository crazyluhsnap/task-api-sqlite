from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app=FastAPI(
    title="Task Management API",
    description="""
A simple CRUD API built using FastAPI

Features: 
- Create Tasks
- Read Tasks
- Update Tasks
- Delete Tasks

Data is stored in memory.
    """,
    version="1.0.0"
)

tasks=[
    {
        "id":1,
        "title":"Complete assignment",
        "done":False
    },
    {
        "id":2,
        "title":"Go to gym",
        "done":True
    },
    {
        "id":3,
        "title":"Practice DSA",
        "done":False
    }
]

class TaskCreate(BaseModel):
    title: str=Field(
        ...,
        example="Buy Groceries",
        description="Title of the task"
    )

class TaskUpdate(BaseModel):
    title: str=Field(
        ...,
        example="Buy Groceries"
    )
    done: bool=Field(
        ...,
        example=False
    )

@app.get("/",
         summary="Get API information",
         description="Returns basic information about the API.")
def home():
    return {
        "name":"Fast API",
        "version":"1.0",
        "endpoints":[
            "/tasks"
        ]
    }

@app.get("/health",
         summary="Health Check",
         description="Checks whether the server is running.")
def health():
    return{
        "status":"ok"
    }

@app.get("/tasks",
         summary="Get all tasks",
         description="Returns the complete list of tasks stored in memory.")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}",
         summary="Get task by ID",
         description="Returns a task using its ID.")
def get_task(task_id: int):
    for task in tasks:
        if task["id"]==task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )

@app.post("/tasks",
          status_code=201,
          summary="Create a new task",
          description="Creates a new task.")
def create_task(task: TaskCreate):

    if task.title.strip()=="":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    new_task={
        "id": len(tasks)+1,
        "title": task.title,
        "done":False
    }
    tasks.append(new_task)

    return new_task

@app.put("/tasks/{task_id}",
         summary="Update a task",
         description="Updates an existing task.")
def update_task(task_id: int, updated_task: TaskUpdate):

    if(updated_task.title.strip()==""):
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    for task in tasks:

        if task["id"]==task_id:
            task["title"]=updated_task.title
            task["done"]=updated_task.done

            return task

    raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

@app.delete("/tasks/{task_id}",
            status_code=204, 
            summary="Delete a task",
            description="Deletes a task.")
def delete_task(task_id: int):

    for index, task in enumerate(tasks):
        if task["id"]==task_id:
            tasks.pop(index)
            return

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )