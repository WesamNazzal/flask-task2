from repositories.shared.base_repository import BaseRepository
from infrastructure.database.schema.schema import books
from sqlalchemy.sql import select, insert, update, delete
from repositories.unit_of_work import UnitOfWork


class BookRepository(BaseRepository):

    def __init__(self):
        super().__init__(books)

    def _add(self, uow: UnitOfWork, data: dict):
        query = insert(self.table).values(data)
        uow.conn.execute(query)

    def _get_all(self, uow: UnitOfWork):
        result = uow.conn.execute(select(self.table)).fetchall()
        return [dict(row) for row in result]

    def _get_by_id(self, uow: UnitOfWork, book_id):
        result = uow.conn.execute(select(self.table).where(self.table.c.book_id == book_id)).fetchone()
        return dict(result) if result else None

    def _update(self, uow: UnitOfWork, book_id, data: dict):
        query = update(self.table).where(self.table.c.book_id == book_id).values(data)
        uow.conn.execute(query)

    def _delete(self, uow: UnitOfWork, book_id):
        query = delete(self.table).where(self.table.c.book_id == book_id)
        uow.conn.execute(query)
