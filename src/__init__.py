from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.books.routes import book_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server starting...")
    await init_db()  # initialize the database connection here (e.g., PostgreSQL, SQLite, etc.)

    yield
    print("Server shutting doen...")
    


app = FastAPI(
    title="Book Service",
    description="An API for managing a Book service with FastAPI and SQLAlchemy",
    version="1.0.0",
    lifespan=lifespan
)


app.include_router(book_router, tags=["books"])