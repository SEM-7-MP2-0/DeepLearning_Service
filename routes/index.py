from flask import Blueprint

index = Blueprint(name="index", import_name=__name__)


@index.route("", methods=["GET"])
def index_handler():
    return "Hello Welcome to Face Detection API!!"
