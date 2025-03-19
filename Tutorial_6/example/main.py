from fastapi import FastAPI
"""
FastAPI application with basic endpoints.

This module sets up a FastAPI application with two endpoints:
- Root endpoint ("/") that returns a hello world message

The @ symbol is a decorator in Python that modifies the behavior of functions:
- @app.get("/") specifies that the following function handles HTTP GET requests at the root path

Dependencies:
    - FastAPI
    - uvicorn
    - typing.Optional

Usage:
    Run the application using:
    `fastapi dev main.py`
    This will start the server on host 0.0.0.0:8000
"""

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
