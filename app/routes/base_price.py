from flask import Blueprint, request, jsonify
from app.controllers import base_price_controller

base_price = Blueprint("base_price", __name__)


@base_price.route("/get_baseprice", methods=["GET"])
def get_base_price():
    response = base_price_controller.get_data()
    return response


@base_price.route("/insert_baseprice", methods=["POST"])
def insert_base_price():
    data = request.json
    response = base_price_controller.create_data(data)
    return response
