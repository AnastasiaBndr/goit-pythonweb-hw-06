from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from .models import Student, Teacher, Grade, Group, Discipline
from .configuration import engine


def task1():
    with Session(engine) as session:
        try:
            top_students = (
                session.query(
                    Grade.student_id,
                    func.avg(Grade.grade).label("average_grade")
                )
                .group_by(Grade.student_id)
                .order_by(desc("average_grade"))
                .limit(5)
                .all()
            )

            for student_id, avg_grade in top_students:
                student = session.get(Student, student_id)
                print(f"{student.name}: {avg_grade:.2f}")

        except:
            session.rollback()
            raise
        else:
            session.commit()


def task2(discipline):
    with Session(engine) as session:
        try:
            top_students = (
                session.query(
                    Grade.student_id,
                    func.avg(Grade.grade).label("average_grade")
                )
                .filter(Grade.discipline_id == discipline)
                .group_by(Grade.student_id)
                .order_by(desc("average_grade"))
                .limit(1)
                .all()
            )

            for student_id, avg_grade in top_students:
                student = session.get(Student, student_id)
                print(f"{student.name}: {avg_grade:.2f}")

        except:
            session.rollback()
            raise
        else:
            session.commit()


def task3(discipline):
    with Session(engine) as session:
        try:
            group_avg_grades = (
                session.query(
                    Group.group_name,
                    func.avg(Grade.grade).label("average_grade")
                )
                .join(Group.students)       
                .join(Student.grades)
                .filter(Grade.discipline_id == discipline)
                .group_by(Group.id)
                .all()
            )

            for group,avg_grade in group_avg_grades:
                print(f"{group}: {avg_grade:.2f}")

        except:
            session.rollback()
            raise
        else:
            session.commit()


def task4():
    with Session(engine) as session:
        try:
            group_avg = (
                session.query(
                    func.avg(Grade.grade)
                )
                .select_from(Grade)
                .scalar()
            )

            print(f"{group_avg:.2f}")

        except:
            session.rollback()
            raise
        else:
            session.commit()


def task5(teacher):
    with Session(engine) as session:
        try:
            disciplines = (
                session.query(
                    Discipline.discipline_name
                )
                .select_from(Discipline)
                .filter(Discipline.teacher_id == teacher).all()
            )

            for dis in disciplines:
                print(f"{dis}")

        except:
            session.rollback()
            raise
        else:
            session.commit()


def task6(group):
    with Session(engine) as session:
        try:
            disciplines = (
                session.query(
                    Student.name
                ).filter(Student.group_id==group)
                .all()
            )

            for stud in disciplines:
                print(f"{stud}")

        except:
            session.rollback()
            raise
        else:
            session.commit()


def task7(group,discipline):
    with Session(engine) as session:
        try:
            disciplines = (
                session.query(
                    Discipline.discipline_name
                )
                .select_from(Discipline)
                .filter(Discipline.teacher_id == teacher).all()
            )

            for dis in disciplines:
                print(f"{dis}")

        except:
            session.rollback()
            raise
        else:
            session.commit()
