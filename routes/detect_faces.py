import uuid
import numpy as np
import cv2
from flask import Blueprint, request, jsonify
from helper import detect_faces as detect_faces_helper

detect_faces = Blueprint(name="detect_faces", import_name=__name__)


@detect_faces.route("", methods=["POST"])
def detect_faces_handler():
    if request.method == "POST":
        try:
            image_file = request.files["image"]
            if image_file:
                allowed_extensions = {"jpg", "jpeg", "png"}
                if image_file.filename.split(".")[-1] not in allowed_extensions:
                    return jsonify({"message": "Invalid file type"}), 400
                image = cv2.imdecode(
                    np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR
                )
                image_path = "./output/" + str(uuid.uuid4()) + ".jpg"
                # save image to disk

                cv2.imwrite(image_path, image)
                original_image = cv2.imread(image_path)
                image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
                img, count = detect_faces_helper(original_image, image)
                cv2.imwrite(image_path, img)

                return (
                    jsonify(
                        {
                            "message": "Faces Detected Successfully",
                            "image": image_path,
                            "face_count": count,
                        }
                    ),
                    200,
                )
            return jsonify({"message": "No image found"}), 400
        except Exception as e:
            print(e)
            return jsonify({"message": "Something went wrong"}), 500
    return "Hello Welcome to Face Detection API"
