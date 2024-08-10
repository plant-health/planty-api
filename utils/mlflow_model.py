"MLflow util"

import mlflow

MODEL_NAME = "Planty"
mlflow.set_tracking_uri("http://192.168.0.75:5000")
client = mlflow.tracking.MlflowClient()
latest_version_info = client.get_latest_versions(MODEL_NAME)
latest_version = latest_version_info[0].version
model_uri = f"models:/{MODEL_NAME}/Production"


def get_mlflow_model():
    "MLflow get latest model"

    return mlflow.pyfunc.load_model(model_uri)
