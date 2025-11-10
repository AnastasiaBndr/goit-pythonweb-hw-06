ENTRYPOINT = main.py

add:
	git add .

commit:
	git commit -m "${name}"
push:
	git push origin main

run:
 	docker run --name goit-hw-python-web-DB -p 5432:5432 -e POSTGRES_PASSWORD=homeworkpassword -d postgres

compose:
	docker compose up -d

autogenerate:
	alembic revision --autogenerate -m "${name}"

head:
	alembic upgrade head