from typing import Generic, TypeVar

from sqlalchemy.sql.schema import Table

from infrastructure.repositories.shared.base_repository import BaseRepository
from presentation.exceptions.app_exception import AppException

T = TypeVar('T', bound=Table)


class BaseService(Generic[T]):

    def __init__(self, repository: BaseRepository[T]):
        self.repo = repository

    def get_all(self) -> tuple[list[dict[str, object]], int]:
        return self.repo.get_all(), 200

    def get_by_id(self, record_id: int) -> tuple[dict[str, object], int]:
        if (record := self.repo.get(record_id)) is None:
            raise AppException('Record not found', 404)
        return record, 200

    def create(self, data: dict[str, object]) -> tuple[dict[str, object], int]:
        if (record := self.repo.create(data)) is None:
            raise AppException('Failed to create record', 500)
        return record, 201

    def update(self, record_id: int, data: dict[str, object]) -> tuple[dict[str, object], int]:
        if (record := self.repo.update(record_id, data)) is None:
            raise AppException('Record not found', 404)
        return record, 200

    def delete(self, record_id: int) -> tuple[dict[str, object], int]:
        if not self.repo.delete(record_id):
            raise AppException('Record not found', 404)
        return {}, 204
