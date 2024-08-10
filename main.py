"Flask app main file"

import json
import uuid
import time
from flask import Flask, jsonify, Response, g, request
import config
from blueprints.model import model_blueprint


def create_app():
    "Build flask app server funciton"

    flask_app = Flask(__name__)
    flask_app.register_blueprint(model_blueprint, url_prefix="/api/v1/model")

    # after request message include in all calls to server
    @flask_app.after_request
    def after_request(response):
        if response and response.get_json():
            data = response.get_json()

            data["time_request"] = int(time.time())
            data["version"] = config.VERSION

            response.set_data(json.dumps(data))

        return response

    @flask_app.before_request
    def before_request_func():
        execution_id = uuid.uuid4()
        g.start_time = time.time()
        g.execution_id = execution_id

        print(g.execution_id, "ROUTE CALLED ", request.url)

    @flask_app.route("/version", methods=["GET"], strict_slashes=False)
    def version():
        response_body = {
            "success": 1,
        }
        return jsonify(response_body)

    # Error 404 handler
    @flask_app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404

    # Error 401 handler
    @flask_app.errorhandler(401)
    def custom_401():
        return Response("API Key required.", 401)

    return flask_app


app = create_app()


if __name__ == "__main__":

    print(" -------- Starting planty server... --------")
    print(" ------ Know plants, know results ^-^ ------")
    app.run(host="0.0.0.0", port=5050)
