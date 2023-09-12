from flask import Blueprint, request, jsonify
from app.controllers import brand_controller

brand = Blueprint("brand", __name__)


@brand.route("/get_brand", methods=["GET"])
def get_manufacturer():
    response = brand_controller.get_data()
    return response


@brand.route("/insert_brand", methods=["POST"])
def insert_manufacturer():
    data = request.json
    response = brand_controller.create_data(data)
    return response
