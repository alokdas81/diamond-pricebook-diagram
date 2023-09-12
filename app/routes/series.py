from flask import Blueprint, request, jsonify
from app.controllers import series_controller

series = Blueprint("series", __name__)


@series.route("/get_series", methods=["GET"])
def get_series():
    response = series_controller.get_data()
    return response


@series.route("/insert_series", methods=["POST"])
def insert_series():
    data = request.json
    response = series_controller.create_data(data)
    return response
