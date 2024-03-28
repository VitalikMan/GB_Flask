# Задание 1:
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.
import random
from flask import Flask, render_template
from Task_2.models import db, Book, Author, BookAuthor


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase_books.db"
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")


@app.cli.command("add-book")
def add_data():
    for i in range(1, 10):
        book = Book(name=f"name_{i}", year=i + 2000, count=i)
        db.session.add(book)

    for i in range(1, 10):
        author = Author(
            firstname=f"firstname_{i}",
            lastname=f"lastname_{i}",
        )
        db.session.add(author)
    db.session.commit()

    for i in range(1, 15):
        book_author = BookAuthor(
            book_id=random.randint(1, 9),
            author_id=random.randint(1, 14),
        )
        db.session.add(book_author)
    db.session.commit()
    print("Данные добавлены")


@app.route("/books/")
def get_books():
    book = Book.query.all()
    context = {"books": book}
    return render_template("books.html", **context)
