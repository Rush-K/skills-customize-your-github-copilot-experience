# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API in Python with FastAPI, create routes, validate request data, and return JSON responses. This assignment introduces the core ideas behind modern web APIs in a beginner-friendly way.

## 📝 Tasks

### 🛠️ Set Up the FastAPI App

#### Description
Create a basic FastAPI application and verify that it runs locally. Start by creating a simple health check endpoint that confirms the service is working.

#### Requirements
Completed program should:

- Install and import FastAPI
- Create an app instance using `FastAPI()`
- Add a `GET` endpoint at `/health`
- Return a JSON response such as `{"status": "ok"}`
- Run the app with Uvicorn or another local server

### 🛠️ Build a Simple Resource API

#### Description
Create an API for managing a list of items, such as books, products, or tasks. The student should implement endpoints to read and create items.

#### Requirements
Completed program should:

- Create at least one data model for an item
- Add a `GET` endpoint to return all items
- Add a `POST` endpoint to create a new item
- Return JSON data in a consistent format
- Store items in an in-memory list for this assignment

### 🛠️ Validate Inputs and Improve the API

#### Description
Improve the API by validating incoming data with Pydantic models and adding clear response behavior.

#### Requirements
Completed program should:

- Define a request model with required fields and types
- Reject invalid input data before storing it
- Add a route to fetch a single item by its ID
- Return helpful error responses when a requested item is not found
- Demonstrate that the API responds with JSON for both success and failure cases
