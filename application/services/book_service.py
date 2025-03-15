from typing import Any, Dict, List, Tuple
from sqlalchemy.sql.schema import Table
from application.services.shared.base_service import BaseService
from infrastructure.repositories.book_repository import BookRepository
from presentation.exceptions.app_exception import AppException

class BookService(BaseService[Table]):
    def __init__(self) -> None:
        super().__init__(BookRepository())

    def borrow_book(self, book_id: int, member_id: int) -> Tuple[Dict[str, Any], int]:
        book = self.repo.get_book_by_id(book_id)
        if not book:
            raise AppException('Book not found', 404)

        if book['is_borrowed']:
            raise AppException('Book is already borrowed', 400)

        update_data = {'is_borrowed': True, 'borrowed_by': member_id}
        updated_book = self.repo.update_book(book_id, update_data)
        if not updated_book:
            raise AppException('Failed to update book', 500)
        return updated_book, 200

    def return_book(self, book_id: int) -> Tuple[Dict[str, Any], int]:
        book = self.repo.get_book_by_id(book_id)
        if not book:
            raise AppException('Book not found', 404)

        if not book['is_borrowed']:
            raise AppException('Book is not borrowed', 400)

        update_data = {'is_borrowed': False, 'borrowed_by': None}
        updated_book = self.repo.update_book(book_id, update_data)
        if not updated_book:
            raise AppException('Failed to update book', 500)
        return updated_book, 200

    def get_book_by_id(self, book_id: int) -> Tuple[Dict[str, Any], int]:
        book = self.repo.get_book_by_id(book_id)
        if not book:
            raise AppException('Book not found', 404)
        return book, 200

    def update_book(self, book_id: int, data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        updated_book = self.repo.update_book(book_id, data)
        if not updated_book:
            raise AppException('Book not found', 404)
        return updated_book, 200

    def delete_book(self, book_id: int) -> Tuple[Dict[str, Any], int]:
        if not self.repo.delete_book(book_id):
            raise AppException('Book not found', 404)
        return {'message': 'Book deleted successfully'}, 200
