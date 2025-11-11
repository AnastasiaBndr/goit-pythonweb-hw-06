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
                f"{teacher_name.name}: {avg_grade}")
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

            print(f"Student {student_name.name} visits courses:")
            for (course_name,) in courses:
                print(f"- {course_name}")

        except:
            session.rollback()
            raise
        else:
            session.commit()


def select_10(student, teacher):
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
                f"Student {student_name.name} attends {teacher_name.name}'s courses:")

            for (course_name,) in courses:
                print(f"- {course_name}")

        except:
            session.rollback()
            raise
        else:
            session.commit()


""" PART 2 """


def select11(teacher, student):
    with Session(engine) as session:
        try:
            teacher_marks = (
                session.query(
                    Teacher.name.label("teacher_name"),
                    Student.name.label("student_name"),
                    func.avg(Grade.grade).label("avg_grade")
                )
                .select_from(Grade)
                .join(Grade.discipline)
                .join(Discipline.teacher)
                .join(Grade.student)
                .filter(Teacher.id == teacher, Student.id == student)
                .group_by(Teacher.id, Student.id)
                .order_by(Teacher.name, Student.name)
                .all()
            )

            for teach, stud, mark in teacher_marks:
                print(f"Teacher: {teach}\nStudent: {stud}\nMark: {mark}")

        except:
            session.rollback()
            raise
        else:
            session.commit()


def select12(group, discipline):
    with Session(engine) as session:
        try:
            last_date = (
                session.query(func.max(Grade.date_received))
                .select_from(Grade)
                .join(Grade.student)
                .join(Student.group)
                .join(Grade.discipline)
                .filter(Group.id == group)
                .filter(Discipline.id == discipline)
                .scalar()
            )

            teacher_marks = (
                session.query(
                    Group.group_name.label("Group"),
                    Discipline.discipline_name,
                    Student.name.label("Student"),
                    Grade.grade.label("Grade"),
                    Grade.date_received
                )
                .join(Grade.student)
                .join(Student.group)
                .join(Grade.discipline)
                .filter(Group.id == group, Discipline.id == discipline, Grade.date_received == last_date)
                .all()
            )

            for teach in teacher_marks:
                print(f"{teach}")

        except:
            session.rollback()
            raise
        else:
            session.commit()
