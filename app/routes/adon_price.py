from flask import Blueprint, request, jsonify
from app.controllers import adon_price_controller

adon_price = Blueprint("adon_price", __name__)


@adon_price.route("/get_adonprice", methods=["GET"])
def get_adon_price():
    response = adon_price_controller.get_data()
    return response


@adon_price.route("/insert_adonprice", methods=["POST"])
def insert_adon_price():
    data = request.json
    response = adon_price_controller.create_data(data)
    return response
