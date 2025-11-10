import random
from sqlalchemy.orm import Session
from .configuration import engine
from .models import Group, Student, Grade, Teacher, Discipline
from datetime import date,timedelta
from faker import Faker
from .faker_providers import disciplines_provider

faker = Faker()
faker.add_provider(disciplines_provider)


def fillGroup(number: int):

    with Session(engine) as session:
        session.begin()
        try:
            session.add_all([Group(group_name=f"Group-{i+1}")
                            for i in range(number)])
        except:
            session.rollback()
            raise
        else:
            session.commit()


def fillStudent(number: int):

    with Session(engine) as session:
        session.begin()
        try:
            group_ids = [group.id for group in session.query(Group.id).all()]
            session.add_all([Student(name=faker.name(), group_id=random.choice(
                group_ids))for _ in range(number)])
        except:
            session.rollback()
            raise
        else:
            session.commit()


def fillTeacher(number: int):

    with Session(engine) as session:
        session.begin()
        try:
            session.add_all([Teacher(name=faker.name())
                            for _ in range(number)])
        except:
            session.rollback()
            raise
        else:
            session.commit()


def fillDiscipline(number=8):

    with Session(engine) as session:
        session.begin()
        try:
            teacher_ids = [
                teacher.id for teacher in session.query(Teacher.id).all()]
            session.add_all([Discipline(discipline_name=faker.unique.disciplines(), teacher_id=random.choice(
                teacher_ids))for _ in range(number)])
        except:
            session.rollback()
            raise
        else:
            session.commit()


def fillGrades():
    with Session(engine) as session:
        session.begin()
        try:
            student_ids = [
                student.id for student in session.query(Student.id).all()]
            discipline_ids = [
                discipline.id for discipline in session.query(Discipline.id).all()]

            semester_start = date(2025, 9, 1) 
            semester_end = date(2025, 12, 31)

            all_dates = [semester_start + timedelta(days=i) 
            for i in range((semester_end - semester_start).days + 1)]
            grades_to_add = []

            for student_id in student_ids:
                possible_combinations = [(d, dt)
                                        for d in discipline_ids for dt in all_dates]

                chosen_combinations = random.sample(
                    possible_combinations, min(20, len(possible_combinations)))

                for discipline_id, grade_date in chosen_combinations:
                    grades_to_add.append(
                        Grade(
                            grade=random.randint(60,100),
                            student_id=student_id,
                            discipline_id=discipline_id,
                            date_received=grade_date
                        )
                    )


            session.add_all(grades_to_add)
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()


def clearAllData():
    with Session(engine) as session:
        session.begin()
        try:
            session.query(Grade).delete()
            session.query(Discipline).delete()
            session.query(Teacher).delete()
            session.query(Student).delete()
            session.query(Group).delete()
        except:
            session.rollback()
            raise
        else:
            session.commit()
