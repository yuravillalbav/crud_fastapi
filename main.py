from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get('/books/', status_code=status.HTTP_200_OK)
def get_books(session: Session = Depends(get_session)):
    itemBook = session.query(models.Books).all()
    return itemBook


@app.get("/books/{id}", status_code=status.HTTP_200_OK)
def get_book(id: int, session: Session = Depends(get_session)):
    itemBook = session.query(models.Books).get(id)
    return itemBook


@app.post("/books/", status_code=status.HTTP_201_CREATED)
def add_book(item: schemas.Book, session: Session = Depends(get_session)):
    itemBook = models.Books(id=item.id, title=item.title, author=item.author, age=item.age)
    session.add(itemBook)
    session.commit()
    session.refresh(itemBook)
    return itemBook


@app.put("/books/{id}", status_code=status.HTTP_200_OK)
def update_book(id: int, item: schemas.Book, session: Session = Depends(get_session)):
    itemBook = session.query(models.Books).get(id)
    itemBook.id = item.id
    itemBook.title = item.title
    itemBook.author = item.author
    itemBook.age = item.age
    session.commit()
    return itemBook


@app.delete("/books{id}", status_code=status.HTTP_200_OK)
def delete_book(id: int, session: Session = Depends(get_session)):
    itemBook = session.query(models.Books).get(id)
    session.delete(itemBook)
    session.commit()
    session.close()
    return 'Book was deleted!'