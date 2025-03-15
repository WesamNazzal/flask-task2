from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Table

from infrastructure.database.connection.connection import metadata

books = Table(
    'books',
    metadata,
    Column('book_id', Integer, primary_key=True, autoincrement=True),
    Column('title', String, nullable=False),
    Column('author', String, nullable=False),
    Column('is_borrowed', Boolean, default=False),
    Column('borrowed_date', DateTime, nullable=True),
    Column('borrowed_by', Integer, ForeignKey('members.member_id', ondelete="SET NULL"), nullable=True)  # 🔥 Fix FK
)

members = Table(
    'members',
    metadata,
    Column('member_id', Integer, primary_key=True, autoincrement=True),  # ✅ Ensure autoincrement works
    Column("name", String, nullable=False),
    Column("email", String, unique=True, nullable=False),
)
