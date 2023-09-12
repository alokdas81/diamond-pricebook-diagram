from flask import Blueprint, request, jsonify
from app.controllers import base_price_controller

baseprice = Blueprint("baseprice", __name__)


@baseprice.route("/get_baseprice", methods=["GET"])
def get_baseprice():
    response = base_price_controller.get_data()
    return response


@baseprice.route("/insert_baseprice", methods=["POST"])
def insert_baseprice():
    data = request.json
    response = base_price_controller.create_data(data)
    return response
