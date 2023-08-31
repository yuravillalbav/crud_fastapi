from sqlalchemy.orm import Session
import models, schemas

def get_books(session: Session, skip: int = 0, limit: int = 100):
    return session.query(models.Books).offset(skip).limit(limit).all()

def get_book(session: Session, book_id: int):
    return session.query(models.Books).filter(models.Books.id == book_id).first()


def create_book(session:Session, book: schemas.Book):
    new_book = models.Books(title=book.title, author=book.author, age=book.age)
    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    return new_book
#MALOOOOOOO
def update_book(session:Session, book: schemas.Book, ):
    db_book = get_book(session=session,  )
    db_book.title = book.title
    db_book.author = book.author
    db_book.age = book.age
    session.commit()
    session.refresh(db_book)
    return db_book

def delete_book(session:Session, book_id: int):
    db_book = get_book(session=session, book_id=book_id)
    session.delete(db_book)
    session.commit()