from flask import Flask

app = Flask(__name__)

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


# Задание 3
@app.route("/string/<string:name>")
def text(name: str) -> str:
    return str(len(name))


if __name__ == "__main__":
    app.run(debug=True)
