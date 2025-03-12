from sqlalchemy import create_engine, MetaData
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://myuser:mypassword@localhost/library_db')

engine = create_engine(DATABASE_URL, echo=True)

metadata = MetaData()


def get_connection():
    return engine.connect()


def create_tables():
    from infrastructure.database.schema.schema import metadata
    metadata.create_all(engine)
