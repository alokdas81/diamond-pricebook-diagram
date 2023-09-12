from flask import Blueprint, request, jsonify
from app.controllers import adon_feature_controller

adonFeature = Blueprint("adonFeature", __name__)


@adonFeature.route("/get_adonFeatures", methods=["GET"])
def get_manufacturer():
    response = adon_feature_controller.get_data()
    return response


@adonFeature.route("/insert_adonFeatures", methods=["POST"])
def insert_manufacturer():
    data = request.json
    response = adon_feature_controller.create_data(data)
    return response
