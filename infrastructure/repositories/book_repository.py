from typing import Any, Dict, List, Optional

from sqlalchemy.sql import delete, select, update
from sqlalchemy.sql.schema import Table

from infrastructure.database.schema.schema import books
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
            return [dict(row._mapping) for row in result] if result else []

    def is_book_borrowed(self, book_id: int) -> bool:
        with UnitOfWork() as uow:
            result = uow.connection.execute(
                select(self.table.c.is_borrowed).where(self.table.c.book_id == book_id)
            ).scalar()
            return bool(result)

    def get_book_by_id(self, book_id: int) -> Optional[Dict[str, Any]]:
        with UnitOfWork() as uow:
            result = uow.connection.execute(
                select(self.table).where(self.table.c.book_id == book_id)
            ).mappings().first()
            return dict(result) if result else None

    def update_book(self, book_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        with UnitOfWork() as uow:
            stmt = (
                update(self.table)
                .where(self.table.c.book_id == book_id)
                .values(**data)
                .returning(self.table)
            )
            result = uow.connection.execute(stmt).mappings().first()
            uow.commit()
            return dict(result) if result else None

    def delete_book(self, book_id: int) -> bool:
        with UnitOfWork() as uow:
            stmt = delete(self.table).where(self.table.c.book_id == book_id)
            result = uow.connection.execute(stmt)
            uow.commit()
            return result.rowcount > 0
