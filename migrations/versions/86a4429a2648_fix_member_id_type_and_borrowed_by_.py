"""Fix member_id type and borrowed_by foreign key

Revision ID: 86a4429a2648
Revises: 
Create Date: 2025-03-16 01:13:07.911781

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '86a4429a2648'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('members',
    sa.Column('member_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('member_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('books',
    sa.Column('book_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('author', sa.String(), nullable=False),
    sa.Column('is_borrowed', sa.Boolean(), nullable=True),
    sa.Column('borrowed_date', sa.DateTime(), nullable=True),
    sa.Column('borrowed_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['borrowed_by'], ['members.member_id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('book_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    op.drop_table('members')
    # ### end Alembic commands ###
