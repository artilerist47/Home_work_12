from flask import Blueprint, render_template, request

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
    picture_path = "/" + save_picture(picture)
    post = add_post({"pic": picture_path, "content": content})
    return render_template("post_uploaded.html", post=post)