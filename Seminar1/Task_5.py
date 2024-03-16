from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

# # Задание 1
# @app.route('/')
# def index():
#     return 'Hello World!'
#
# # Задание 2
# @app.route('/about/')
# def about():
#     return 'about'
#
#
# @app.route('/contact/')
# def contact():
#     return 'contact'
#
#
# @app.route('/<int:num_1>/<int:num_2>')
# def sum_nums(num_1, num_2) -> str:
#     return str(num_1 + num_2)
#
# # Задание 3
# @app.route('/string/<string:name>')
# def text(name: str) -> str:
#     return str(len(name))
#
# # Задание 4
# @app.route('/world')
# def world():
#     return render_template('index.html')

# Задание 5
@app.route('/students/')
def students():
    head = {
        'name': 'Имя',
        'lastname': 'Фамилия',
        'age': 'Возраст',
        'rating': 'Средний балл'
    }
    students_list = [
        {
            'name': 'Иван',
            'lastname': 'Иванов',
            'age': 18,
            'rating': 4
        },
        {
            'name': 'Петр',
            'lastname': 'Петров',
            'age': 19,
            'rating': 3
        },
        {
            'name': 'Семен',
            'lastname': 'Семенов',
            'age': 20,
            'rating': 5
        }
    ]
    return render_template('index.html', **head, students_list=students_list)


if __name__ == '__main__':
    app.run(debug=True)
