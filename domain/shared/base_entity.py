import uuid
from abc import ABC, abstractmethod
from datetime import datetime


class BaseEntity(ABC):
    def __init__(self, entity_id: str | None = None) -> None:
        self.id = entity_id or self.generate_id()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @staticmethod
    def generate_id() -> str:
        return str(uuid.uuid4())

    def update_timestamp(self) -> None:
        self.updated_at = datetime.now()

    @abstractmethod
    def to_dict(self) -> dict[str, object]:
        pass
