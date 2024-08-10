"Predict service"

import base64
import io
from PIL import Image
import numpy as np
from utils.mlflow_model import get_mlflow_model
from constants.categories import MODEL_CATEGORIES

model = get_mlflow_model()


def predict(image):
    "Predict method"

    image_buf = io.BytesIO(base64.b64decode(image))
    image = Image.open(image_buf)
    image = image.resize((224, 224))

    image = np.expand_dims(image, axis=0)

    predictions = model.predict(image)

    index = np.argmax(predictions[0])
    category = MODEL_CATEGORIES[index]

    print(category)

    return 1, category
