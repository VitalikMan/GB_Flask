from flask import Flask, render_template

app = Flask(__name__)

# # Задание 1
# @app.route('/')
# def index():
#     return 'Hello World!'


# Задание 2
@app.route("/about/")
def about():
    return "about"


@app.route("/contact/")
def contact():
    return "contact"


@app.route("/<int:num_1>/<int:num_2>")
def sum_nums(num_1, num_2) -> str:
    return str(num_1 + num_2)


if __name__ == "__main__":
    app.run()
