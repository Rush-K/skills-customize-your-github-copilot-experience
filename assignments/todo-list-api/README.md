# 📘 Assignment: To-Do List API with SQLite

## 🎯 Objective

Build a small task management API using FastAPI and SQLite. Students will learn how to create REST endpoints, save data to a database, and handle basic CRUD operations in a practical application.

## 📝 Tasks

### 🛠️ Create the FastAPI App and Database

#### Description
Set up a FastAPI project that stores tasks in a SQLite database and exposes a health check endpoint.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Connect to a SQLite database file such as `tasks.db`
- Create a `tasks` table with fields like `id`, `title`, and `completed`
- Add a `GET /health` endpoint that returns a JSON status response
- Confirm the database and API start correctly when the app runs

### 🛠️ Add CRUD Endpoints

#### Description
Implement the main task operations so students can create, read, update, and delete to-do items through HTTP requests.

#### Requirements
Completed program should:

- Add a `GET /tasks` endpoint to list all tasks
- Add a `POST /tasks` endpoint to create a new task
- Add a `GET /tasks/{task_id}` endpoint to fetch one task by ID
- Add a `PUT /tasks/{task_id}` endpoint to update an existing task
- Add a `DELETE /tasks/{task_id}` endpoint to remove a task
- Return JSON responses using consistent data structure

### 🛠️ Validate Data and Improve Error Handling

#### Description
Make the API more robust by validating input and handling missing tasks cleanly.

#### Requirements
Completed program should:

- Validate required task fields before saving data
- Reject invalid or incomplete task payloads
- Return a clear 404 error when a task ID does not exist
- Prevent invalid updates from breaking the database
- Show that the API behaves correctly for both success and error cases
