from typing import Any, Dict, Optional

from sqlalchemy.sql import select

from infrastructure.database.schema.schema import members
from infrastructure.repositories.shared.base_repository import BaseRepository
from infrastructure.repositories.unit_of_work import UnitOfWork


class MemberRepository(BaseRepository):

    def __init__(self):
        super().__init__(members)

    def get_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        with UnitOfWork() as uow:
            result = uow.connection.execute(
                select(self.table).where(self.table.c.email == email)
            ).mappings().first()
            return dict(result) if result else None

    def get_by_id(self, member_id: int) -> Optional[Dict[str, Any]]:
        with UnitOfWork() as uow:
            result = uow.connection.execute(
                select(self.table).where(self.table.c.member_id == member_id)
            ).mappings().first()
        return dict(result) if result else None
