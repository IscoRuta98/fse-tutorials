from fastapi import FastAPI, HTTPException, Path, Query
from models import Book, BookRequest
from starlette import status

# Initialize the FastAPI application
app = FastAPI()

# Dummy data for the books API (list of Book objects)
BOOKS = [
    Book(
        1,
        "The Great Gatsby",
        "F. Scott Fitzgerald",
        "A classic novel about the American Dream",
        4,
        1925,
    ),
    Book(
        2,
        "To Kill a Mockingbird",
        "Harper Lee",
        "A Pulitzer Prize-winning novel about racial injustice",
        5,
        1960,
    ),
    Book(
        3,
        "Harry Potter and the Philosopher's Stone",
        "J.K. Rowling",
        "The first book in the popular fantasy series",
        4,
        1997,
    ),
    Book(
        4,
        "The Catcher in the Rye",
        "J.D. Salinger",
        "A controversial novel about teenage rebellion",
        3,
        1951,
    ),
    Book(
        5,
        "Pride and Prejudice",
        "Jane Austen",
        "A classic romance novel set in 19th century England",
        5,
        1813,
    ),
    Book(
        6,
        "The Hobbit",
        "J.R.R. Tolkien",
        "A fantasy novel about a hobbit's adventure",
        4,
        1937,
    ),
]


# Define the endpoints for the books API
@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


# Define the endpoint to get a specific book by its ID
@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


# Define the endpoint to get books by author
@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


# Define the endpoint to get books by publish date
@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_books_by_publish_date(published_date: int = Query(gt=1800, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return


@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")
