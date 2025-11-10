from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg://postgres:homeworkpassword@localhost:5432/university_db"
)
