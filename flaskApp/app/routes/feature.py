from flask import Blueprint, request, jsonify
from app.controllers import feature_controller

feature = Blueprint("feature", __name__)


@feature.route("/get_features", methods=["GET"])
def get_series():
    response = feature_controller.get_data()
    return response


@feature.route("/insert_feature", methods=["POST"])
def insert_series():
    data = request.json
    response = feature_controller.create_data(data)
    return response
