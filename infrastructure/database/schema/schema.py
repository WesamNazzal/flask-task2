from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, ForeignKey
from infrastructure.database.connection.connection import metadata

books = Table(
    'books',
    metadata,
    Column('book_id', Integer, primary_key=True, autoincrement=True),
    Column('title', String, nullable=False),
    Column('author', String, nullable=False),
    Column('is_borrowed', Boolean, default=False),
    Column('borrowed_date', DateTime, nullable=True),
    Column('borrowed_by', String, ForeignKey('members.member_id'), nullable=True)
)


members = Table(
    'members',
    metadata,
    Column('member_id', String, primary_key=True),
    Column('name', String, nullable=False),
    Column('email', String, unique=True, nullable=False)
)
