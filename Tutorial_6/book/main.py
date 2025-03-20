from fastapi import Body, FastAPI

app = FastAPI()

"""
/api-endpoint: A GET request that returns a JSON object with a message "Hello World".
"""


@app.get("/api-endpoint")
async def first_api():
    return {"message": "Hello World"}


# Dummy Data
BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]


"""
/books: A GET request that returns a JSON object with a list of all books in the BOOKS list.
"""


@app.get("/books")
async def read_all_books():
    return BOOKS


"""
/books/{book_title}: A GET request that takes a book_title as a path parameter and returns a JSON 
object with the details of the book that matches the given title.
"""


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


"""
/books/: A GET request that takes a category as a query parameter and returns a JSON 
object with a list of all books in the specified category.
"""


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


"""
/books/{book_author}/: A GET request that takes a book_author and a category 
as query parameters and returns a JSON object with a list of all books by the 
specified author in the specified category.
"""


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (
            book.get("author").casefold() == book_author.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            books_to_return.append(book)

    return books_to_return


"""
/books/create_book: A POST request that takes a JSON object as the request body 
and adds the new book to the BOOKS list.
"""


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


"""
/books/update_book: A PUT request that takes a JSON object as the request body, 
finds the book with the matching title, and updates its details.
"""


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book


"""
/books/delete_book/{book_title}: A DELETE request that takes a book_title as a path 
parameter and removes the book from the BOOKS list.
"""


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
