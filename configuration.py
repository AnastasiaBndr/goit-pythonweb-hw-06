from sqlalchemy import create_engine, String, Boolean, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine("sqlite:///bookshelf.db", echo=True)


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    author: Mapped[str] = mapped_column(String(50), nullable=False)
    is_read: Mapped[bool] = mapped_column(Boolean, default=False)

    def __str__(self):
        return f"Book({self.id}, {self.title}, {self.author})"


def add_book(book_title: str, book_author: str):
    with Session(engine) as session:
        book = Book(title=book_title, author=book_author)
        session.add(book)
        session.commit()
        print(f"Книгу '{book.title}' збережено")


def delete_author(author_id: int):
    pass


def list_all_books():
    with Session(engine) as session:
        books = session.query(Book).all()
        for book in books:
            print(book)


def count_all_books() -> int:
    with engine.connect() as connection:
        count_query = select(func.count(Book.id))
        result = connection.execute(count_query)
        return result.scalar_one()


def mark_book_as_read(book_id: int):
    with Session(engine) as session:
        book = session.get(Book, book_id)
        if not book:
            print("Книгу не знайдено!")
            return
        book.is_read = True
        session.commit()

