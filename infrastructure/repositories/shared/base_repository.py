from typing import TypeVar, Generic, List, Dict
from repositories.unit_of_work import UnitOfWork
from abc import ABC, abstractmethod

T = TypeVar('T')


class BaseRepository(Generic[T]):

    def __init__(self, table):
        self.table = table

    def add(self, data: Dict):
        with UnitOfWork() as uow:
            self._add(uow, data)
            uow.commit()

    def get_all(self) -> List[Dict]:
        with UnitOfWork() as uow:
            return self._get_all(uow)

    def get_by_id(self, entity_id) -> Dict:
        with UnitOfWork() as uow:
            return self._get_by_id(uow, entity_id)

    def update(self, entity_id, data: Dict):
        with UnitOfWork() as uow:
            self._update(uow, entity_id, data)
            uow.commit()

    def delete(self, entity_id):
        with UnitOfWork() as uow:
            self._delete(uow, entity_id)
            uow.commit()

    @abstractmethod
    def _add(self, uow: UnitOfWork, data: Dict):
        pass

    @abstractmethod
    def _get_all(self, uow: UnitOfWork) -> List[Dict]:
        pass

    @abstractmethod
    def _get_by_id(self, uow: UnitOfWork, entity_id) -> Dict:
        pass

    @abstractmethod
    def _update(self, uow: UnitOfWork, entity_id, data: Dict):
        pass

    @abstractmethod
    def _delete(self, uow: UnitOfWork, entity_id):
        pass
