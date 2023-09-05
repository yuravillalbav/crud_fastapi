from fastapi import FastAPI, HTTPException
from database import engine, create_db_and_tables
from models import Book
from sqlmodel import Session, select

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post('/books')
def create_book(book: Book):
    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)
        return book

@app.get('/books')
def read_books():
    with Session(engine) as session:
        books = session.exec(select(Book)).all()
        return books

@app.get('/books/{book_id}')
def read_book(book_id: int):
    with Session(engine) as session:
        book = session.get(Book, book_id)
        if not book:
            raise HTTPException(status_code=404, detail='Book not found!')
        return book

@app.patch('/books/{book_id}')
def update_book(book_id: int, book: Book):
    with Session(engine) as session:
        db_book = session.get(Book, book_id)
        if not db_book:
            raise HTTPException(status_code=404, detail='Book not found!')
        book_data = book.dict(exclude_unset=True)
        for key, value in book_data.items():
            setattr(db_book, key, value)
        session.add(db_book)
        session.commit()
        session.refresh(db_book)
        return db_book

@app.delete('/books/{book_id}')
def delete_book(book_id: int):
    with Session(engine) as session:
        book = session.get(Book, book_id)
        if not book:
            raise HTTPException(status_code=404, detail='Book not found')
        session.delete(book)
        session.commit()
        return {'ok': True}