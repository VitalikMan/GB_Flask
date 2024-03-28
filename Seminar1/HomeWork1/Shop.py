# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.
from flask import Flask, render_template, request

app = Flask(__name__)

clothes = [
    ["group", "name", "desc", "id"],
    [
        "Футболки",
        "Классическая футболка",
        'Описание "Классическая футболка"',
        "tshirt_classic",
    ],
    [
        "Футболки",
        "Принтованная футболка",
        'Описание "Принтованная футболка"',
        "tshirt_printed",
    ],
    ["Джинсы", "Скинни джинсы", 'Описание "Скинни джинсы"', "jeans_skinny"],
    ["Джинсы", "Прямые джинсы", 'Описание "Прямые джинсы"', "jeans_straight"],
    ["Платья", "Коктейльное платье", 'Описание "Коктейльное платье"', "dress_cocktail"],
    ["Платья", "Вечернее платье", 'Описание "Вечернее платье"', "dress_evening"],
]


def parse_clothes_to_dict() -> list:
    res = []
    for val_lst_index in range(1, len(clothes)):
        new_dict = {}
        for i in range(len(clothes[0])):
            new_dict[clothes[0][i]] = clothes[val_lst_index][i]
        res.append(new_dict)
    return res


@app.route("/")
def index():
    context = {
        "title": "Главная",
    }
    return render_template("index.html", **context)


@app.route("/categories/")
def categories():
    _clothes = parse_clothes_to_dict()
    context = {
        "title": "Категории",
        "categories": [
            "Футболки",
            "Джинсы",
            "Платья",
        ],
        "clothes": _clothes,
    }
    return render_template("categories.html", **context)


@app.route("/about/")
def about():
    context = {
        "title": "О нас",
    }
    return render_template("about.html", **context)


@app.route("/contacts/")
def contacts():
    context = {
        "title": "Контакты",
    }
    return render_template("contacts.html", **context)


@app.route("/clothes/item/", methods=["GET", "POST"])
def item():
    selected_item = request.args.get("selected_from_cats")
    _clothes = parse_clothes_to_dict()
    show_item = {}
    for item_dict in _clothes:
        if item_dict["name"] == selected_item:
            show_item = dict(item_dict)
    context = {
        "title": "Карточка товара",
        "selected": selected_item,
        "item": show_item,
    }
    return render_template("item.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
