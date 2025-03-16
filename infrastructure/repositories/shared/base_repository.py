from typing import Any, Dict, Generic, List, Optional, TypeVar

from sqlalchemy import delete, insert, select, update
from sqlalchemy.sql.schema import Table

from infrastructure.repositories.unit_of_work import UnitOfWork

T = TypeVar('T')


class BaseRepository(Generic[T]):

    def __init__(self, table: Table) -> None:
        self.table: Table = table
        self.primary_key: str = self.table.primary_key.columns.values()[0].name

    def get_all(self) -> List[Dict[str, Any]]:
        with UnitOfWork() as uow:
            result = uow.connection.execute(select(self.table)).mappings().all()
            return [dict(row) for row in result] if result else []

    def get(self, record_id: int) -> Optional[Dict[str, Any]]:
        with UnitOfWork() as uow:
            result = uow.connection.execute(
                select(self.table).where(self.table.c[self.primary_key] == record_id)
            ).mappings().first()
            return dict(result) if result else None

    def create(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        with UnitOfWork() as uow:
            stmt = insert(self.table).values(**data).returning(self.table)
            result = uow.connection.execute(stmt).mappings().first()
            uow.commit()
            return dict(result) if result else None

    def update(self, record_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
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
