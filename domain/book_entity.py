from datetime import datetime

from domain.shared.base_entity import BaseEntity


class BookEntity(BaseEntity):
    def __init__(
        self,
        title: str,
        author: str,
        is_borrowed: bool = False,
        borrowed_by: str | None = None,
        borrowed_date: datetime | None = None,
        book_id: str | None = None,
    ) -> None:
        super().__init__(book_id)
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by
        self.borrowed_date = borrowed_date

    def to_dict(self) -> dict[str, object]:
        return {
            'book_id': self.id,
            'title': self.title,
            'author': self.author,
            'is_borrowed': self.is_borrowed,
            'borrowed_by': self.borrowed_by,
            'borrowed_date': self.borrowed_date.strftime('%Y-%m-%d %H:%M:%S') if self.borrowed_date else None,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        }
