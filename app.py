from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

model = load_model("cat_dog_classifier_model.h5")

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    img_path = ""

    if request.method == "POST":
        file = request.files["file"]
        img_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(img_path)

        img = image.load_img(img_path, target_size=(256,256))
        img = image.img_to_array(img)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        result = model.predict(img)

        if result[0][0] > 0.5:
            prediction = "Dog 🐶"
        else:
            prediction = "Cat 🐱"

    return render_template("index.html", prediction=prediction, img_path=img_path)

if __name__ == "__main__":
    app.run(debug=True)