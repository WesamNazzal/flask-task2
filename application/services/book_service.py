from datetime import datetime

from sqlalchemy.sql.schema import Table

from application.services.shared.base_service import BaseService
from infrastructure.repositories.book_repository import BookRepository
from presentation.exceptions.app_exception import AppException


class BookService(BaseService[Table]):
    def __init__(self) -> None:
        super().__init__(BookRepository())

    def borrow_book(self, book_id: int, member_id: int) -> tuple[dict[str, object], int]:
        if not (book := self.repo.get(book_id)):
            raise AppException('Book not found', 404)

        if book['is_borrowed']:
            raise AppException('Book is already borrowed', 400)

        update_data = {'is_borrowed': True, 'borrowed_by': member_id, 'borrowed_date': datetime.now()}
        if not (updated_book := self.repo.update(book_id, update_data)):
            raise AppException('Failed to update book', 500)

        return updated_book, 200

    def return_book(self, book_id: int) -> tuple[dict[str, object], int]:
        if not (book := self.repo.get(book_id)):
            raise AppException('Book not found', 404)

        if not book['is_borrowed']:
            raise AppException('Book is not borrowed', 400)

        update_data = {'is_borrowed': False, 'borrowed_by': None}
        if not (updated_book := self.repo.update(book_id, update_data)):
            raise AppException('Failed to update book', 500)

        return updated_book, 200

    def get_book_by_id(self, book_id: int) -> tuple[dict[str, object], int]:
        if not (book := self.repo.get(book_id)):
            raise AppException('Book not found', 404)

        return book, 200

    def update_book(self, book_id: int, data: dict[str, object]) -> tuple[dict[str, object], int]:
        if not self.repo.get(book_id):
            raise AppException('Book not found', 404)

        updated_book = self.repo.update(book_id, data)

        return updated_book, 200

    def delete_book(self, book_id: int) -> tuple[dict[str, object], int]:
        if not self.repo.delete(book_id):
            raise AppException('Book not found', 404)

        return {'message': 'Book deleted successfully'}, 200

    def get_borrowed_book_with_member(self, book_id: int) -> tuple[dict[str, object], int]:
        if not (book_info := self.repo.get_borrowed_book_with_member(book_id)):
            raise AppException('Book not Found or not borrowed', 404)

        return book_info, 200
