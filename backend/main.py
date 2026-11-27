
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database table
def init_db():
    conn = sqlite3.connect("todo.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Home
@app.get("/")
def home():
    return {"message": "SQLite Backend Running!"}

# Get tasks
@app.get("/tasks")
def get_tasks():
    conn = sqlite3.connect("todo.db")
    rows = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()

    return {
        "tasks": [
            {
                "id": row[0],
                "task": row[1],
                "completed": bool(row[2])
            }
            for row in rows
        ]
    }

# Add task
@app.post("/tasks")
def add_task(task: str):
    conn = sqlite3.connect("todo.db")
    cursor = conn.execute(
        "INSERT INTO tasks (task) VALUES (?)", (task,)
    )
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()

    return {"id": task_id, "task": task, "completed": False}

# Delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn = sqlite3.connect("todo.db")
    cursor = conn.execute(
        "DELETE FROM tasks WHERE id = ?", (task_id,)
    )
    conn.commit()
    deleted = cursor.rowcount
    conn.close()

    return {"message": "Deleted" if deleted else "Task not found"}

# Complete / uncomplete task
@app.patch("/tasks/{task_id}")
def complete_task(task_id: int):
    conn = sqlite3.connect("todo.db")
    conn.execute("""
        UPDATE tasks
        SET completed = CASE WHEN completed = 0 THEN 1 ELSE 0 END
        WHERE id = ?
    """, (task_id,))
    conn.commit()

    row = conn.execute(
        "SELECT * FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()
    conn.close()

    if row is None:
        return {"message": "Task not found"}

    return {
        "id": row[0],
        "task": row[1],
        "completed": bool(row[2])
    }

