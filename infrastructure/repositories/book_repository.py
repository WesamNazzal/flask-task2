from typing import Any, Dict, List
from sqlalchemy.sql import select
from sqlalchemy.sql.schema import Table
from infrastructure.database.schema.schema import books, members
from infrastructure.repositories.shared.base_repository import BaseRepository
from infrastructure.repositories.unit_of_work import UnitOfWork


class BookRepository(BaseRepository[Table]):
    def __init__(self) -> None:
        super().__init__(books)

    def get_books_by_author(self, author: str) -> List[Dict[str, Any]]:
        with UnitOfWork() as uow:
            result = uow.connection.execute(
                select(self.table).where(self.table.c.author == author)
            )
            return [dict(row) for row in result.mappings().all()] if result else []

    def is_book_borrowed(self, book_id: int) -> bool:
        with UnitOfWork() as uow:
            return bool(
                uow.connection.execute(
                    select(self.table.c.is_borrowed).where(self.table.c.book_id == book_id)
                ).scalar()
            )

    def get_borrowed_book_with_member(self, book_id: int) -> Dict[str, Any] | None:
        with UnitOfWork() as uow:
            result = uow.connection.execute(
                select(
                    books.c.book_id,
                    books.c.title,
                    books.c.author,
                    books.c.is_borrowed,
                    members.c.name.label("borrowed_by_name")
                ).join(
                    members, books.c.borrowed_by == members.c.member_id
                ).where(books.c.book_id == book_id)
            ).mappings().first()

            return dict(result) if result else None
