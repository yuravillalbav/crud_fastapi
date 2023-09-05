from sqlmodel import SQLModel, create_engine

database_sqlite = 'crud_api.db'
url = f'sqlite:///./{database_sqlite}'

connect_args = {'check_same_thread': False}
engine = create_engine(url, connect_args= connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)