"Model blueprint"

from flask import Blueprint, jsonify, request
from services.predict import predict

model_blueprint = Blueprint(name="model", import_name=__name__)


@model_blueprint.route("/", methods=["GET"], strict_slashes=False)
def get_model_version():
    "Get model version controller"
    return {"model_version": "1.0.0"}


@model_blueprint.route(
    "/predict",
    methods=["POST"],
    strict_slashes=False,
)
def prediction():
    "Predict controller"

    request_body = request.get_json()

    is_success, response = predict(request_body["image"])

    response_body = {
        "success": is_success,
        "data": response if is_success else {"message": str(response)},
    }

    return jsonify(response_body)
