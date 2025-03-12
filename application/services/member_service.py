from application.services.shared.base_service import BaseService
from infrastructure.repositories.member_repository import MemberRepository


class MemberService(BaseService):

    def __init__(self):
        super().__init__(MemberRepository())

    def validate_email(self, email: str):
        members = self.repository.get_all()
        if any(member["email"] == email for member in members):
            raise ValueError("Email already exists.")

    def create_member(self, data: dict):
        self.validate_email(data["email"])
        return self.repository.add(data)

    def get_all_members(self):
        return self.repository.get_all()

    def get_member_by_id(self, member_id: str):
        member = self.repository.get_by_id(member_id)
        if not member:
            raise ValueError("Member not found.")
        return member

    def update_member(self, member_id: str, data: dict):
        existing_member = self.repository.get_by_id(member_id)
        if not existing_member:
            raise ValueError("Member not found.")
        return self.repository.update(member_id, data)

    def delete_member(self, member_id: str):
        existing_member = self.repository.get_by_id(member_id)
        if not existing_member:
            raise ValueError("Member not found.")
        return self.repository.delete(member_id)
