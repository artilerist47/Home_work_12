from flask import Blueprint, render_template, request
from json import JSONDecodeError

from function import add_post
from loader.utils import save_picture

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


@loader_blueprint.route("/post")
def post_page():
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def page_add_post():
    picture = request.files.get("picture")
    content = request.form.get("content")

    if not picture or not content:
        if not content and not picture:
            return "Нет файла и текста"
        elif not picture:
            return "Нет файла"
        return "Нет текста"

    if picture.filename.split(".")[-1] not in ["jpg", "jpeg", "png"]:
        return "Не верный формат файла"

    try:
        picture_path = "/" + save_picture(picture)
    except FileNotFoundError:
        return "Файл не найден"
    except JSONDecodeError:
        return "Файл повреждён или не валиден"
    post = add_post({"pic": picture_path, "content": content})
    return render_template("post_uploaded.html", post=post)
