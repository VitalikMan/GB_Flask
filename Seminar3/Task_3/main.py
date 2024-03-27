# Задание 1:
# Доработаем задача про студентов
# Создать, базу данных для хранения информации о студентах и их оценках в
# учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
# и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название
# предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их оценок.
from flask import Flask, render_template, request
from flask_wtf import CSRFProtect

from Seminar3.Task_3.models import db, Users
from Seminar3.Task_3.forms import RegisterForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_user.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
	db.create_all()
	print('OK')


@app.route('/register/', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if request.method == 'POST' and form.validate():
		username = form.username.data
		email = form.email.data
		password = form.password.data
		user = Users(username=username, email=email, password=password)
		db.session.add(user)
		db.session.commit()
		return f'Вы зарегистрированы'
	return render_template('register.html', form=form)


@app.route('/users/', methods=['GET', 'POST'])
def get_users():
	users = Users.query.all()
	return f'{list(users)}'
