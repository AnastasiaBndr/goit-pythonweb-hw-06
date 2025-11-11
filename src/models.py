from sqlalchemy import String, ForeignKey, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column
from datetime import date


class Base(DeclarativeBase):
    pass


# Many to one


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))

    group: Mapped["Group"] = relationship(back_populates="students")
    grades: Mapped[list["Grade"]] = relationship(
        back_populates="student", cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"Student({self.id}, {self.name})"


# One to many


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    group_name: Mapped[str] = mapped_column(String(10), nullable=False)

    students: Mapped[list["Student"]] = relationship(
        back_populates="group", cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"Group({self.id}, {self.group_name})"


# One to many


class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)

    disciplines: Mapped[list["Discipline"]] = relationship(
        back_populates="teacher", cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"Teacher({self.id}, {self.name})"


# Many to one


class Discipline(Base):
    __tablename__ = "disciplines"

    id: Mapped[int] = mapped_column(primary_key=True)
    discipline_name: Mapped[str] = mapped_column(String(30), nullable=False)
    teacher_id: Mapped["Teacher"] = mapped_column(ForeignKey("teachers.id"))

    teacher: Mapped["Teacher"] = relationship(back_populates="disciplines")
    grades: Mapped[list["Grade"]] = relationship(
        back_populates="discipline", cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"Discipline: ({self.id}, {self.discipline_name}, Teacher: {self.teacher_id})"


# Many to many


class Grade(Base):
    __tablename__ = "grades"

    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), primary_key=True)
    discipline_id: Mapped[int] = mapped_column(
        ForeignKey("disciplines.id"), primary_key=True
    )
    date_received: Mapped[date] = mapped_column(Date, primary_key=True)
    
    grade: Mapped[int] = mapped_column(nullable=False)

    student: Mapped["Student"] = relationship(back_populates="grades")
    discipline: Mapped["Discipline"] = relationship(back_populates="grades")

    def __str__(self):
        return f"Grades: (Student: {self.student_id}, Discipline: {self.discipline_id}, Date: {self.date_received}, Grade: {self.grade})"
