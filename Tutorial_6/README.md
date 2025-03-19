# Building an API using FastAPI

FastAPI is a modern, fast web framework for building APIs with Python 3.6+ based on standard Python type hints. It's designed to be easy to use, fast to code, and ready for production. FastAPI provides automatic API documentation, data validation, and high performance by leveraging Pydantic for data modeling and Starlette for the web toolkit foundation.

**References:**
- [FastAPI Documentation](https://fastapi.tiangolo.com/tutorial/s)

## Quick Start
To start developing with FastAPI:

1. Install the required packages:
```bash
pip install fastapi uvicorn
```

2. Create a basic server:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

3. Run the server:
```bash
uvicorn main:app --reload
```

The server will start on `http://localhost:8000`, and you can access the automatic API documentation at `http://localhost:8000/docs`.

## Async/Await

- `async` marks a function that can be paused and resumed.

- `await` is used to pause execution until a time-consuming operation completes
While waiting, Python can handle other requests


### Real-world Analogy

- Think of a restaurant waiter (your server):

- Synchronous: Waiter takes order → waits at kitchen → delivers food → next customer

- Asynchronous: Waiter takes order → submits to kitchen (await) → serves other customers → picks up food when ready
When to Use

### Main Takeaways

- We use `async def` when your endpoint needs to:
1. Make database queries
2. Call external APIs or
3. Perform I/O operations

You can Use regular `def` for simple, quick operations


**Key Points:**

- FastAPI can handle both async and sync routes
- Async routes don't block the server
- Better performance under high load
- Not necessarily faster for individual requests

### Real world example

#### Database Query
Imagine you have a database and you want to fetch user data asynchronously.

```python
from fastapi import FastAPI
import databases

DATABASE_URL = "sqlite:///./test.db"
database = databases.Database(DATABASE_URL)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    query = "SELECT * FROM users WHERE id = :user_id"
    user = await database.fetch_one(query=query, values={"user_id": user_id})
    return {"user": user}
```

### External API Call
Fetching data from an external API asynchronously.
```python
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/weather/{city}")
async def get_weather(city: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}")
        weather_data = response.json()
    return {"weather": weather_data}
```