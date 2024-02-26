"""This is the main module of the library application."""
from fastapi import FastAPI
from pydantic import BaseModel

from models import RepositoryModel, ControllerModel
from database import db


class ResponseBookModel(BaseModel):
    """A class representing an book in the library."""

    title: str
    author: str
    isbn: str
    year: str
    genre: str


class BookRepository(RepositoryModel):
    """A class representing the book model in the library."""

    collection = db.get_collection("books")


class BookController(ControllerModel):
    """A class representing the book controller in the library."""

    repository = BookRepository()

    def get_books(self, bid: str):
        """Retrieve all books from the database."""
        return self.repository.read(bid)


book_controller = BookController()

app = FastAPI()


@app.get("/")
def index():
    """Get a welcoming message."""
    return {"message": "Hello, world!"}


@app.get(
    "/books/{bid}",
    response_model=ResponseBookModel,
    response_description="Get a book from the library.",
)
def get_books(bid: str):
    """Get all books in the library."""
    return book_controller.get_books(bid)
