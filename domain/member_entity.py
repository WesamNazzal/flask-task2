from typing import Any, Dict

from domain.shared.base_entity import BaseEntity


class MemberEntity(BaseEntity):
    def __init__(self, name: str, email: str, member_id: str | None = None) -> None:
        super().__init__(member_id)
        self.name: str = name
        self.email: str = email

    def to_dict(self) -> Dict[str, Any]:
        return {
            'member_id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        }
