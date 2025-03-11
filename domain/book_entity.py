from domain.shared.base_entity import BaseEntity
from datetime import datetime
from typing import Optional


class BookEntity(BaseEntity):

    def __init__(self, title: str, author: str, is_borrowed: bool = False, borrowed_by: Optional[str] = None, borrowed_date: Optional[datetime] = None, book_id: Optional[int] = None):
        super().__init__(book_id)
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by
        self.borrowed_date = borrowed_date

    def borrow(self, member_id: str):
        if self.is_borrowed:
            raise ValueError("This book is already borrowed.")
        self.is_borrowed = True
        self.borrowed_by = member_id
        self.borrowed_date = datetime.now()
        self.update_timestamp()

    def return_book(self):
        if not self.is_borrowed:
            raise ValueError("This book is not borrowed.")
        self.is_borrowed = False
        self.borrowed_by = None
        self.borrowed_date = None
        self.update_timestamp()

    def to_dict(self):
        return {
            "book_id": self.id,
            "title": self.title,
            "author": self.author,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": self.borrowed_by,
            "borrowed_date": self.borrowed_date.strftime("%Y-%m-%d %H:%M:%S") if self.borrowed_date else None,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
