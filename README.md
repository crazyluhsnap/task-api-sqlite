# Task Management API

A RESTful CRUD API built using **FastAPI** and **SQLite** for managing tasks.

This project is part of the FlyRank Backend Internship (Week 3 Assignment) and demonstrates how to connect a FastAPI CRUD application to a SQLite database. Unlike the previous in-memory implementation, task data is now stored persistently and survives server restarts.

---

## Features

- Create a new task
- View all tasks
- View a task by ID
- Update existing tasks
- Delete tasks
- Persistent storage using SQLite
- Interactive API documentation using Swagger UI

---

## Tech Stack

- Python 3
- FastAPI
- SQLite
- sqlite3
- Pydantic
- Uvicorn

---

## Project Structure

```text
task-api/
│
├── app.py
├── database.py
├── tasks.db
├── requirements.txt
├── README.md
├── .gitignore

```

---

## Installation

Clone the repository

```bash
git clone https://github.com/crazyluhsnap/task-api-sqlite.git
```

Move into the project

```bash
cd task-api
```

Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | API Information |
| GET | /health | Health Check |
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get task by ID |
| POST | /tasks | Create a task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

---

## Database

The application uses **SQLite** for persistent storage.

A local database file named `tasks.db` is automatically created when the application starts for the first time.

The database contains a single table:

| Column | Type |
|---------|------|
| id | INTEGER PRIMARY KEY AUTOINCREMENT |
| title | TEXT |
| done | INTEGER (0 = False, 1 = True) |

On the first run, three sample tasks are automatically inserted into the database.

---

## Sample SQL Queries

```sql
SELECT * FROM tasks;

SELECT COUNT(*) FROM tasks;

UPDATE tasks
SET done = 1
WHERE id = 1;

DELETE FROM tasks
WHERE id = 3;
```

---

## Sample cURL Request

```bash
curl -X POST http://127.0.0.1:8000/tasks ^
-H "Content-Type: application/json" ^
-d "{\"title\":\"Learn SQLite\"}"
```

---

## Screenshots

### Swagger UI

(Add Swagger Screenshot)

### SQLite Database

(Add DB Browser Screenshot)

---

## Learning Outcomes

Through this project I learned:

- Building REST APIs using FastAPI
- Connecting FastAPI with SQLite
- Writing SQL queries (SELECT, INSERT, UPDATE, DELETE)
- Using parameterized SQL queries
- Database persistence
- CRUD operations using SQL
- Working with DB Browser for SQLite

---

