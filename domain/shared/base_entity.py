import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Dict, Optional


class BaseEntity(ABC):
    def __init__(self, entity_id: Optional[str] = None) -> None:
        self.id: str = entity_id or self.generate_id()
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()

    @staticmethod
    def generate_id() -> str:
        return str(uuid.uuid4())

    def update_timestamp(self) -> None:
        self.updated_at = datetime.now()

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass
