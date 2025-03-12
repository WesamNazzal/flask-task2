from typing import TypeVar, Generic, List, Dict
from infrastructure.repositories.shared.base_repository import BaseRepository

T = TypeVar('T')


class BaseService(Generic[T]):

    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def create(self, data: Dict):
        return self.repository.add(data)

    def get_all(self) -> List[Dict]:
        return self.repository.get_all()

    def get_by_id(self, entity_id) -> Dict:
        return self.repository.get_by_id(entity_id)

    def update(self, entity_id, data: Dict):
        return self.repository.update(entity_id, data)

    def delete(self, entity_id):
        return self.repository.delete(entity_id)
