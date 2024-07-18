from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from src.db.models import Book


class BookService:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_all_books(self):
        statement = select(Book).order_by(Book.created_at)
        return await self.session.exec(statement).all()

