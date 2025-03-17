from typing import Any, Dict, Tuple
from sqlalchemy.sql.schema import Table
from application.services.shared.base_service import BaseService
from infrastructure.repositories.member_repository import MemberRepository
from presentation.exceptions.app_exception import AppException


class MemberService(BaseService[Table]):
    def __init__(self) -> None:
        super().__init__(MemberRepository())

    def create_member(self, data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        if missing_fields := [field for field in ['name', 'email'] if field not in data]:
            raise AppException(f"Missing required fields: {', '.join(missing_fields)}", 400)

        if self.repo.get_by_email(data['email']):
            raise AppException('Email already exists', 400)

        try:
            return self.create(data), 201
        except Exception as e:
            raise AppException(f"Database error: {str(e)}", 500)

    def update_member(self, member_id: int, data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        if not self.repo.get_by_id(member_id):

            raise AppException('Member not found', 404)

        return self.update(member_id, data), 200

    def delete_member(self, member_id: int) -> Tuple[Dict[str, Any], int]:
        if not self.repo.get_by_id(member_id):
            raise AppException('Member not found', 404)

        self.delete(member_id)
        return {}, 204

    def get_member_by_email(self, email: str) -> Tuple[Dict[str, Any], int]:
        if not (member := self.repo.get_by_email(email)):
            raise AppException('Member not found', 404)

        return member, 200
