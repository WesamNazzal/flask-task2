from abc import ABC, abstractmethod
import uuid
from datetime import datetime


class BaseEntity(ABC):
    def __init__(self, entity_id=None):
        self.id = entity_id or self.generate_id()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @staticmethod
    def generate_id():
        return str(uuid.uuid4())

    def update_timestamp(self):
        self.updated_at = datetime.now()

    @abstractmethod
    def to_dict(self):
        pass
