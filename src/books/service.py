from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .schemas import BookCreateModel
from src.db.models import Book


class BookService:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_all_books(self):
        statement = select(Book).order_by(Book.created_at)
        result = await self.session.exec(statement) 
        return result.all()
    
    async def create_book(self, book_data:BookCreateModel):
        new_book  = Book(**book_data.model_dump())
        self.session.add(new_book)
        await self.session.commit()
        return new_book
    
    async def get_book(self, book_uuid:str): 
        statement = select(Book).where(Book.uuid == book_uuid)
        result = await self.session.exec(statement)
        return result.first()
    
    async def update_book(self, book_uuid: str, book_data: BookCreateModel):
        # book = await self.get_book(book_uuid)
        # if book:
        #     book.title = book_data.title
        #     book.author = book_data.author
        #     book.isbn = book_data.isbn
        #     book.description = book_data.description
        #     await self.session.commit()
        #     return book
        # return None
        statement = select(Book).where(Book.uuid == book_uuid)
        result = await self.session.exec(statement)
        book = result.first()

        for key, value in book_data.model_dump().items():
            setattr(book, key, value)

        await self.session.commit()
        return book
        
    async def delete_book(self, book_uuid:str):
        statement = select(Book).where(Book.uuid == book_uuid)
        result = await self.session.exec(statement)
        book = result.first()

        await self.session.delete(book)
        await self.session.commit()

        return True


