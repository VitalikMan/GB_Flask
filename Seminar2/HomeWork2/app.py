from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)


# Страница для ввода имени и электронной почты
@app.route("/")
def authorization():
    return render_template("authorization.html")


# Установка cookie-файла с данными пользователя
@app.route("/set_cookie", methods=["POST"])
def set_cookie():
    name = request.form["name"]
    email = request.form["email"]
    response = make_response(redirect("/welcome"))
    response.set_cookie("username", name)
    return response


# Страница приветствия
@app.route("/welcome")
def welcome():
    username = request.cookies.get("username")
    return render_template("main.html", username=username)


# Удаление cookie-файла
@app.route("/delete_cookie", methods=["POST"])
def delete_cookie():
    response = make_response(redirect("/"))
    response.set_cookie("username", "", expires=0)
    return response


if __name__ == "__main__":
    app.run(debug=True)
