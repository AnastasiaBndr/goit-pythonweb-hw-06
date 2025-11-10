from src.seed import fillGroup, clearAllData, fillStudent, fillTeacher, fillDiscipline, fillGrades
from src.my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8,select_9,select_10


def main():
    # select_1()
    # select_2(1)
    # select_3(4)
    # select_4()
    # select_5(3)
    # select_6(2)
    # select_7(1,1)
    # select_8(4)
    # select_9(1)
    # select_10(1,2)

    # clearAllData()
    # fillGroup(3)
    # fillStudent(30)
    # fillTeacher(5)
    # fillDiscipline()
    # fillGrades()

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
    main()
