from typing import Generic, Mapping, TypeVar

from sqlalchemy import delete, insert, select, update
from sqlalchemy.sql.schema import Table

from infrastructure.repositories.unit_of_work import UnitOfWork

T = TypeVar('T')


class BaseRepository(Generic[T]):
    def __init__(self, table: Table) -> None:
        self.table = table
        self.primary_key = self.table.primary_key.columns.values()[0].name

    def get_all(self) -> list[dict[str, object]]:
        with UnitOfWork() as uow:
            result = uow.connection.execute(select(self.table)).mappings().all()
            return [dict(row) for row in result] if result else []

    def get(self, record_id: int) -> dict[str, object] | None:
        with UnitOfWork() as uow:
            result = uow.connection.execute(
                select(self.table).where(self.table.c[self.primary_key] == record_id)
            ).mappings().first()
            return dict(result) if result else None

    def create(self, data: dict[str, object]) -> dict[str, object] | None:
        with UnitOfWork() as uow:
            stmt = insert(self.table).values(**data).returning(self.table)
            result = uow.connection.execute(stmt).mappings().first()
            uow.commit()
            return dict(result) if result else None

    def update(self, record_id: int, data: Mapping[str, object]) -> dict[str, object] | None:
        with UnitOfWork() as uow:
            stmt = (
                update(self.table)
                .where(self.table.c[self.primary_key] == record_id)
                .values(**data)
                .returning(self.table)
            )
            result = uow.connection.execute(stmt).mappings().first()
            uow.commit()

            return dict(result) if result else None

    def delete(self, record_id: int) -> bool:
        with UnitOfWork() as uow:
            stmt = delete(self.table).where(self.table.c[self.primary_key] == record_id)
            result = uow.connection.execute(stmt)
            uow.commit()
            return result.rowcount > 0
