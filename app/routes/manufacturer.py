from flask import Blueprint, request, jsonify
from app.controllers import manufacturer_controller

manufacturer = Blueprint("manufacturer", __name__)


@manufacturer.route("/get_manufacturer", methods=["GET"])
def get_manufacturer():
    response = manufacturer_controller.get_data()
    return response


@manufacturer.route("/insert_manufacturer", methods=["POST"])
def insert_manufacturer():
    data = request.json
    response = manufacturer_controller.create_data(data)
    return response
