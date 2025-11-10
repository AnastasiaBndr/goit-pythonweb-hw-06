import argparse
from sqlalchemy.orm import Session
from src.configuration import engine
from src.seed import autoFill
from src.instanses import create_instance, list_instances, update_instance, delete_instance


def get_kwargs(args):
    """Формує словник аргументів для CRUD-операцій."""
    fields = {
        "name": args.name,
        "group_name": args.name if args.model == "Group" else None,
        "group_id": args.group_id,
        "teacher_id": args.teacher_id,
        "discipline_id": args.discipline_id,
        "student_id": args.student_id,
        "grade": args.grade,
    }
    return {k: v for k, v in fields.items() if v is not None}


def handle_action(session, args):
    """Обробляє CRUD-дію."""
    actions = {
        "create": lambda: create_instance(session, args.model, **get_kwargs(args)),
        "list": lambda: list_instances(session, args.model),
        "update": lambda: update_instance(session, args.model, args.id, **get_kwargs(args)) if args.id else print("❗ Потрібно вказати --id для update"),
        "remove": lambda: delete_instance(session, args.model, args.id) if args.id else print("❗ Потрібно вказати --id для remove"),
    }

    action_func = actions.get(args.action)
    if action_func:
        action_func()
    else:
        print("❌ Невідома дія!")


def main():
    # autoFill()

    parser = argparse.ArgumentParser(
        description="CLI для керування базою студентів")
    parser.add_argument("-a", "--action", choices=["create", "list", "update", "remove"], required=True,
                        help="CRUD операція: create, list, update, remove")
    parser.add_argument("-m", "--model", required=True,
                        help="Назва моделі: Group, Student, Teacher, Discipline, Grade")
    parser.add_argument("--id", type=int, help="ID запису (для update/delete)")
    parser.add_argument(
        "--name", type=str, help="Ім'я або назва (Teacher, Student, Group, Discipline)")
    parser.add_argument("--group_id", type=int, help="ID групи (для Student)")
    parser.add_argument("--teacher_id", type=int,
                        help="ID викладача (для Discipline)")
    parser.add_argument("--discipline_id", type=int,
                        help="ID предмета (для Grade)")
    parser.add_argument("--student_id", type=int,
                        help="ID студента (для Grade)")
    parser.add_argument("--grade", type=int, help="Оцінка (для Grade)")

    args = parser.parse_args()

    with Session(engine) as session:
        handle_action(session, args)


if __name__ == "__main__":
    main()
