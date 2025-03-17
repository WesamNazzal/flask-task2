from typing import Type

from sqlalchemy.engine.base import Connection

from infrastructure.database.connection.connection import engine


class UnitOfWork:
    def __init__(self) -> None:
        self.connection: Connection = engine.connect()
        self.transaction = self.connection.begin()

    def commit(self) -> None:
        self.transaction.commit()

    def rollback(self) -> None:
        self.transaction.rollback()

    def close(self) -> None:
        self.connection.close()

    def __enter__(self) -> 'UnitOfWork':
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: object | None
    ) -> None:
        if exc_type:
            self.rollback()
        self.close()
