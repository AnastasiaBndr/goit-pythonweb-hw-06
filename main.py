from configuration import (
    engine,
    Base,
    add_book,
    list_all_books,
    count_all_books,
    mark_book_as_read,
    delete_author,
)


def main():
    while True:
        print("Меню:")
        print("1. Додати книгу")
        print("2. Переглянути усі книги")
        print("3. Порахувати кількість книжок")
        print("4. Позначити книгу прочитаною")
        print("5. Видалити автора")
        print("6. Вийти з додатку")

        choice = int(input("Оберіть дію 1-6: "))

        if choice == 1:
            title = input("Введіть назву книги:")
            author = input("Введіть імʼя автора книги:")
            add_book(title, author)

        elif choice == 2:
            list_all_books()

        elif choice == 3:
            print(f"Кількість книжок {count_all_books()}")

        elif choice == 4:
            book_id = int(input("Введіть id книги: "))
            mark_book_as_read(book_id)

        elif choice == 5:
            author_id = int(input("Введіть id автора: "))
            delete_author(author_id)

        elif choice == 6:
            print("До побачення!")
            break


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    main()
