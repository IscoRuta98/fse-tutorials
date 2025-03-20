from sqlmodel import Field, SQLModel


class Todo(SQLModel, table=True):
    """
    This class is used to define the structure of the database table
    The table will have three columns: id, task_title, and completed
    The id column is the primary key of the table
    The task_title column will store the title of the task
    The completed column will store the completion status of the task
    """

    id: int | None = Field(default=None, primary_key=True)
    task_title: str = Field(index=True)
    completed: bool = Field(default=False, index=True)


class TodoResponse(SQLModel):
    """
    This class is used to define the structure of the response body for a task
    The id field will store the id of the task
    The task_title field will store the title of the task
    The completed field will store the completion status of the task
    """

    id: int
    task_title: str
    completed: bool


class CreateTodo(SQLModel):
    """
    This class is used to define the structure of the request body for creating a new task
    The task_title field is required and will store the title of the task
    The completed field is optional and will store the completion status of the task
    """

    task_title: str = Field(index=True)
    completed: bool = Field(default=False, index=True)


class UpdateTodo(SQLModel):
    """
    This class is used to define the structure of the request body for updating an existing task
    The task_title field is optional and will store the new title of the task
    The completed field is optional and will store the new completion status of the task
    """

    task_title: str | None = Field(index=True)
    completed: bool | None = Field(index=True)


class DeleteTodo(SQLModel):
    """
    This class is used to define the structure of the request body for deleting a task
    The id field is required and will store the id of the task to be deleted
    """

    id: int
