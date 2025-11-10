from sqlalchemy.orm import Session
from sqlalchemy import func,desc
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
                .filter(Grade.discipline_id==discipline)
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
                    Student.group_id,
                    func.avg(Grade.grade).label("average_grade")
                )
                .join(Grade,Grade.student_id==Student.id)
                .filter(Grade.discipline_id == discipline)
                .group_by(Student.group_id)
                .all()
            )

            for group_id, avg_grade in group_avg_grades:
                group = session.get(Group, group_id)
                print(f"{group.group_name}: {avg_grade:.2f}")

        except:
            session.rollback()
            raise
        else:
            session.commit()
