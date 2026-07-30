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
          description="Creates a new task in the SQLite database.")
def create_task(task: TaskCreate):

    if task.title.strip()=="":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    cursor.execute(
        """
            INSERT INTO tasks(title, done)
            VALUES (?, ?)
        """,
        (task.title,0)
    )

    connection.commit()

    task_id = cursor.lastrowid

    return {
        "id":task_id,
        "title":task.title,
        "done":False
    }

@app.put("/tasks/{task_id}",
         summary="Update a task",
         description="Updates an existing task in the SQLite database."
         )
def update_task(task_id: int, updated_task: TaskUpdate):

    if(updated_task.title.strip()==""):
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    cursor.execute(
        """
            UPDATE tasks
            SET title = ?, done = ?
            WHERE id = ?
        """,
        (
            updated_task.title,
            int(updated_task.done),
            task_id
        )
    )

    connection.commit()

    if cursor.rowcount==0:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    return {
        "id":task_id,
        "title":updated_task.title,
        "done": updated_task.done
    }

@app.delete("/tasks/{task_id}",
            status_code=204, 
            summary="Delete a task",
            description="Deletes a task from the SQLite database.")
def delete_task(task_id: int):

    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )

    connection.commit()

    if cursor.rowcount==0:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )