from sqlalchemy import create_engine, MetaData
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://myuser:mypassword@localhost/library_db')

engine = create_engine(DATABASE_URL, echo=True)


metadata = MetaData()

def create_tables():
    return engine.connect()