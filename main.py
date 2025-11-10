from src.models import engine, Teacher, Student, Grade, Group, Discipline, Base
from src.seed import fill_db


def main():
    while True:
        print("Меню:")
        print("1. Заповнити db")
        print("2. Вийти з додатку")

        choice = int(input("Оберіть дію 1-2: "))

        if choice == 1:
            fill_db()
            print("Заповнено!")

        elif choice == 2:
            print("До побачення!")
            break


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    main()
