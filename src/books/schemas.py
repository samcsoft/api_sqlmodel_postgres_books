from ..db.models import Book
from pydantic import BaseModel


class BooksResponse(BaseModel):
    pass


class BookCreateModel(BaseModel):
    title: str
    author: str
    isbn: str
    description: str

    model_config = {
        "json_schema_extra":{
            "example": {
                "title": "Example Book",
                "author": "Example Author",
                "isbn": "978-3-16-148410-0",
                "description": "This is an example book."
            }
        }
    }

    



