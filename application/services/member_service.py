from sqlalchemy.sql.schema import Table

from application.services.shared.base_service import BaseService
from infrastructure.repositories.member_repository import MemberRepository
from presentation.exceptions.app_exception import AppException


class MemberService(BaseService[Table]):
    def __init__(self) -> None:
        super().__init__(MemberRepository())

    def create_member(self, data: dict[str, object]) -> tuple[dict[str, object], int]:
        if missing_fields := [field for field in ['name', 'email'] if field not in data]:
            raise AppException(f"Missing required fields: {', '.join(missing_fields)}", 400)

        if self.repo.get_by_email(data['email']):
            raise AppException('Email already exists', 400)

        try:
            return self.create(data), 201
        except Exception as e:
            raise AppException(f"Database error: {str(e)}", 500)

    def get_member_by_email(self, email: str) -> tuple[dict[str, object], int]:
        if not (member := self.repo.get_by_email(email)):
            raise AppException('Member not found', 404)

        return member, 200
