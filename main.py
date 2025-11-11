import argparse
from sqlalchemy.orm import Session
from src.configuration import engine
from src.seed import autoFill
from src.instanses import create_instance, list_instances, update_instance, delete_instance


def get_kwargs(args):
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
    actions = {
        "create": lambda: create_instance(session, args.model, **get_kwargs(args)),
        "list": lambda: list_instances(session, args.model),
        "update": lambda: update_instance(session, args.model, args.id, **get_kwargs(args)) if args.id else print("❗ You need to set --id for update"),
        "remove": lambda: delete_instance(session, args.model, args.id) if args.id else print("❗ You need to set --id for remove"),
    }

    action_func = actions.get(args.action)
    if action_func:
        action_func()
    else:
        print("❌ Unknown action!")


def main():
    # autoFill()

    parser = argparse.ArgumentParser(
        description="CLI for db control")
    parser.add_argument("-a", "--action", choices=["create", "list", "update", "remove"], required=True,
                        help="CRUD operation: create, list, update, remove")
    parser.add_argument("-m", "--model", required=True,
                        help="Model name: Group, Student, Teacher, Discipline, Grade")
    parser.add_argument("--id", type=int, help="ID (for update/delete)")
    parser.add_argument(
        "--name", type=str, help="Name (Teacher, Student, Group, Discipline)")
    parser.add_argument("--group_id", type=int, help="Group ID (for Student)")
    parser.add_argument("--teacher_id", type=int,
                        help="Teacher ID (for Discipline)")
    parser.add_argument("--discipline_id", type=int,
                        help="Discipline ID (for Grade)")
    parser.add_argument("--student_id", type=int,
                        help="Student ID (for Grade)")
    parser.add_argument("--grade", type=int, help="Grade (for Grade)")

    args = parser.parse_args()

    with Session(engine) as session:
        handle_action(session, args)


if __name__ == "__main__":
    main()
