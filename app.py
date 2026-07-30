from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from database import cursor, connection

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
         description="Returns all tasks from the SQLite database")
def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    rows=cursor.fetchall()
    tasks=[]

    for row in rows:
        tasks.append({
            "id":row[0],
            "title":row[1],
            "done":bool(row[2])
        })
    return tasks

@app.get("/tasks/{task_id}",
         summary="Get task by ID",
         description="Returns a single task from the SQLite Database.")
def get_task(task_id: int):
    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    row=cursor.fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    return {
        "id":row[0],
        "title":row[1],
        "done":bool(row[2])
    }

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

    new_id = max([task["id"] for task in tasks], default=0) + 1

    new_task={
        "id": new_id,
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