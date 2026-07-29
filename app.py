from fastapi import FastAPI, HTTPException

app=FastAPI(
    title="Task API",
    description="A simple CRUD API for managing tasks",
    version="1.0"
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

@app.get("/", summary="Get API information")
def home():
    return {
        "name":"Fast API",
        "version":"1.0",
        "endpoints":[
            "/tasks"
        ]
    }

@app.get("/health",summary="Health Check")
def health():
    return{
        "status":"ok"
    }

@app.get("/tasks",summary="Get all tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", summary="Get task by ID")
def get_task(task_id: int):
    for task in tasks:
        if task["id"]==task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )