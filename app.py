from fastapi import FastAPI

app=FastAPI(
    title="Task API",
    description="A simple CRUD API for managing tasks",
    version="1.0"
)

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