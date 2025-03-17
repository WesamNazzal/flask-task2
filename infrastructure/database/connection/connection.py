from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import Connection

from config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)

metadata = MetaData()


def get_connection() -> Connection:
    return engine.connect()


def create_tables() -> None:
    from infrastructure.database.schema.schema import metadata
    metadata.create_all(engine)
