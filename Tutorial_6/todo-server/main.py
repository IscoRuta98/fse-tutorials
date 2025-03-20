from typing import Annotated

from fastapi import FastAPI, HTTPException, Query
from starlette import status
from sqlmodel import select
from models import DeleteTodo, TodoDB, TodoResponse, CreateTodo

from db import create_db_and_tables, SessionDep


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# POST /todos
@app.post("/todos/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: CreateTodo, session: SessionDep):
    db_todo = TodoDB.model_validate(todo)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


# GET /todos
@app.get("/todos/", response_model=list[TodoResponse], status_code=status.HTTP_200_OK)
def read_todos(
    session: SessionDep, # Dependency injection of the SessionDep class to get the database session
    offset: int = 0, # Query parameter for the offset of the results to return (default is 0)
    limit: Annotated[int, Query(le=100)] = 100, # Query parameter for the limit of the results to return (default is 100, maximum is 100)
):
    todos = session.exec(select(TodoDB).offset(offset).limit(limit)).all()
    return todos

# GET /todos/by-title
@app.get("/todos/by-title", response_model=TodoResponse, status_code=status.HTTP_200_OK)
def read_todo_by_title(todo_title: str, session: SessionDep):
    todo = session.exec(select(TodoDB).where(TodoDB.task_title == todo_title)).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# GET /todos/completed
@app.get("/todos/completed", response_model=list[TodoResponse], status_code=status.HTTP_200_OK)
def read_completed_todos(session: SessionDep):
    todos = session.exec(select(TodoDB).where(TodoDB.completed == True)).all()
    return todos

# GET /todos/incompleted
@app.get("/todos/incompleted", response_model=list[TodoResponse], status_code=status.HTTP_200_OK)
def read_incompleted_todos(session: SessionDep):
    todos = session.exec(select(TodoDB).where(TodoDB.completed == False)).all()
    return todos

# GET /todos/{todo_id}
@app.get("/todos/{todo_id}", response_model=TodoResponse, status_code=status.HTTP_200_OK)
def read_todo(todo_id: int, session: SessionDep):
    todo = session.get(TodoDB, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# PATCH /todos/{todo_id}
@app.patch("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo: CreateTodo, session: SessionDep):
    todo_db = session.get(TodoDB, todo_id)
    if not todo_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_data = todo.model_dump(exclude_unset=True)
    todo_db.sqlmodel_update(todo_data)
    session.add(todo_db)
    session.commit()
    session.refresh(todo_db)
    return todo_db

# DELETE /todos/{todo_id}
@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, session: SessionDep):
    todo = session.get(TodoDB, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(todo)
    return None
