from application.services.shared.base_service import BaseService
from infrastructure.repositories.book_repository import BookRepository
from datetime import datetime


class BookService(BaseService):

    def __init__(self):
        super().__init__(BookRepository())

    def borrow_book(self, book_id: int, member_id: str):
        book = self.repository.get_by_id(book_id)
        if not book:
            raise ValueError("Book not found.")

        if book["is_borrowed"]:
            raise ValueError("This book is already borrowed.")

        update_data = {
            "is_borrowed": True,
            "borrowed_by": member_id,
            "borrowed_date": datetime.now()
        }
        self.repository.update(book_id, update_data)

    def return_book(self, book_id: int):
        book = self.repository.get_by_id(book_id)
        if not book:
            raise ValueError("Book not found.")

        if not book["is_borrowed"]:
            raise ValueError("This book is not borrowed.")

        update_data = {
            "is_borrowed": False,
            "borrowed_by": None,
            "borrowed_date": None
        }
        self.repository.update(book_id, update_data)
