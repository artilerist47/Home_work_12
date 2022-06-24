from loader.views import loader_blueprint
from main.views import main_blueprint
from flask import Flask, send_from_directory
import logging


app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

logging.basicConfig(filename="basic.log", level=logging.INFO)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
