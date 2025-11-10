from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from .models import Student, Teacher, Grade, Group, Discipline
from .configuration import engine


def select_1():
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


def select_2(discipline):
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


def select_3(discipline):
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

            for group, avg_grade in group_avg_grades:
                print(f"{group}: {avg_grade:.2f}")

        except:
            session.rollback()
            raise
        else:
            session.commit()


def select_4():
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


def select_5(teacher):
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


def select_6(group):
    with Session(engine) as session:
        try:
            disciplines = (
                session.query(
                    Student.name
                ).filter(Student.group_id == group)
                .all()
            )

            for stud in disciplines:
                print(f"{stud}")

        except:
            session.rollback()
            raise
        else:
            session.commit()


def select_7(group, discipline):
    with Session(engine) as session:
        try:
            grades = (
                session.query(
                    Student.name, Grade.grade
                )
                .join(Student.grades)
                .filter(Student.group_id == group)
                .filter(Grade.discipline_id == discipline)
                .all()
            )

            for stud, grade in grades:
                print(f"{stud}: {grade}")

        except:
            session.rollback()
            raise
        else:
            session.commit()


def select_8(teacher):
    with Session(engine) as session:
        try:

            avg_grade = (
                session.query(func.avg(Grade.grade))
                .join(Grade.discipline)
                .filter(Discipline.teacher_id == teacher)
                .scalar()
            )

            teacher_name = session.get(Teacher, teacher)

            print(
                f"Середній бал, який ставить викладач {teacher_name.name}: {avg_grade}")
        except:
            session.rollback()
            raise
        else:
            session.commit()


def select_9(student):
    with Session(engine) as session:
        try:

            courses = (
                session.query(Discipline.discipline_name)
                .join(Grade)
                .filter(Grade.student_id == student)
                .distinct()
                .all()
            )

            student_name = session.get(Student, student)

            print(f"Студент {student_name.name} відвідує курси:")
            for (course_name,) in courses:
                print(f"- {course_name}")

        except:
            session.rollback()
            raise
        else:
            session.commit()


def select_10(student,teacher):
    with Session(engine) as session:
        try:

            courses = (
                session.query(Discipline.discipline_name)
                .join(Grade)
                .filter(Grade.student_id == student)
                .filter(Discipline.teacher_id == teacher)
                .distinct()
                .all()
            )

            student_name = session.get(Student, student)
            teacher_name = session.get(Teacher, teacher)

            print(
                f"Курси, які студент {student_name.name} слухає у викладача {teacher_name.name}:")
            
            for (course_name,) in courses:
                print(f"- {course_name}")

        except:
            session.rollback()
            raise
        else:
            session.commit()
