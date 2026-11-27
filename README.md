# To-Do List Application

A simple full-stack To-Do List application built using HTML, CSS, JavaScript, Python FastAPI, and SQLite.

## Features
- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Store tasks permanently using SQLite

## Technologies Used
- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI
- Database: SQLite

## How to Run

### 1. Start the backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
uvicorn main:app --reload
```

### 2. Start the frontend

Open another terminal:

```bash
cd todo-project
python3 -m http.server 5500
```

Open: http://127.0.0.1:5500

## Developer
Rakesh KK

## License
Not specified.
