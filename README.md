# Task Management API

A RESTful CRUD API built using **FastAPI** and **SQLite** for managing tasks.

This project demonstrates CRUD operations backed by a SQLite database, replacing the earlier in-memory implementation with persistent storage. It includes automatic database initialization, seeded sample data, and interactive API documentation through Swagger UI.

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

<img width="1285" height="454" alt="image" src="https://github.com/user-attachments/assets/0eea28a1-b694-4569-8a4e-7fa6ea372210" />


---

## Database

The application uses **SQLite** for persistent storage.

A local database file named `tasks.db` is automatically created when the application starts for the first time.

The database contains a single table:

<img width="608" height="518" alt="image" src="https://github.com/user-attachments/assets/eafa4b04-a26b-4dbf-8cb8-75ca31e0f42c" />


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
### SQLite Database

<img width="1038" height="658" alt="image" src="https://github.com/user-attachments/assets/1c1923da-384f-458e-8cb0-4182754cc7e2" />

<img width="1038" height="662" alt="image" src="https://github.com/user-attachments/assets/b8b3f662-b4d3-4eb6-854b-bde42907d38d" />

<img width="1030" height="655" alt="image" src="https://github.com/user-attachments/assets/6fd55e27-1329-445b-be8d-1893cda195ad" />

<img width="1038" height="654" alt="image" src="https://github.com/user-attachments/assets/2c0fcfea-308c-4ca5-81a0-14dd722b5f01" />

<img width="1037" height="655" alt="image" src="https://github.com/user-attachments/assets/38e7442b-2d7f-4d1c-ad46-e23f5b1e64da" />

<img width="1033" height="658" alt="image" src="https://github.com/user-attachments/assets/7b77657a-edf5-48a1-8c65-16a2ce975799" />



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

