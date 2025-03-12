from infrastructure.database.connection.connection import get_connection


class UnitOfWork:

    def __enter__(self):
        self.conn = get_connection()
        self.tx = self.conn.begin()
        return self

    def commit(self):
        self.tx.commit()

    def rollback(self):
        self.tx.rollback()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.rollback()

        self.conn.close()
