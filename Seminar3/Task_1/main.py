# Задание 1:
# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
# возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название
# факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.
import random

from flask import Flask, render_template
from Seminar3.Task_1.models import db, Student, Faculty

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")


@app.cli.command("add-student")
def add_data():
    for i in range(1, 3):
        faculty = Faculty(name=f"faculty_{i}")
        db.session.add(faculty)

    for i in range(1, 10):
        student = Student(
            firstname=f"firstname_{i}",
            lastname=f"lastname_{i}",
            gender=random.choice(["муж", "жен"]),
            group=random.randint(1, 5),
            id_faculty=random.randint(1, 3),
        )
        db.session.add(student)
    db.session.commit()
    print("Данные добавлены")


@app.route("/")
def get_student():
    students = Student.query.all()
    context = {"students": students}
    return render_template("students.html", **context)
