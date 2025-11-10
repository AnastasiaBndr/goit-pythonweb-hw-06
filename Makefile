ENTRYPOINT = main.py

run:
 	docker run --name goit-hw-python-web-DB -p 5432:5432 -e POSTGRES_PASSWORD=homeworkpassword -d postgres

compose:
	docker compose up -d

autogenerate:
	alembic revision --autogenerate -m "Generating tables"

head:
	alembic upgrade head