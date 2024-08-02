from typing import Sequence
from google.cloud import vision
from flask import Blueprint, render_template

import os
import json

google_vision_bp = Blueprint('google_vision_bp', __name__)

from google.oauth2 import service_account
import google.auth

# Path to the service account key file
service_account_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
credentials = service_account.Credentials.from_service_account_file(service_account_path)

# Use credentials to initialize Google clients


def analyze_image_from_uri(
    image_uri: str,
    feature_types: Sequence,
) -> vision.AnnotateImageResponse:
    client = vision.ImageAnnotatorClient(credentials=credentials)

    image = vision.Image()
    image.source.image_uri = image_uri
    features = [vision.Feature(type_=feature_type) for feature_type in feature_types]
    request = vision.AnnotateImageRequest(image=image, features=features)

    response = client.annotate_image(request=request)

    return response


def print_labels(response: vision.AnnotateImageResponse):
    print("=" * 80)
    for label in response.label_annotations:
        print(
            f"{label.score:4.0%}",
            f"{label.description:5}",
            sep=" | ",
        )
        

image_uri = "https://cdn.pixabay.com/photo/2024/01/29/20/40/cat-8540772_1280.jpg"
features = [vision.Feature.Type.LABEL_DETECTION]

response = analyze_image_from_uri(image_uri, features)
print_labels(response)

@google_vision_bp.route('/google_vision')
def google_vision():
    return render_template('google.html', labels=response.label_annotations)