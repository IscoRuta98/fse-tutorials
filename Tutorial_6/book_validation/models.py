from typing import Optional

from pydantic import BaseModel, Field


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    # Constructor to initialize the Book class with the given parameters
    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(title="id is not needed")
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=300)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1800, lt=2031)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "A new book",
                "author": "Author Name",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2029,
            }
        }
