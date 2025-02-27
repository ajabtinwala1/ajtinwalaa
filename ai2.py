pip install opencv-python numpy tensorflow keras
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load pre-trained AI model (replace with your model)
model = load_model("pipeline_crack_detector.h5")

# Load and preprocess the image
def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0  # Normalize
    img = np.expand_dims(img, axis=0)
    img = np.expand_dims(img, axis=-1)
    return img

# Detect cracks
def detect_crack(image_path):
    img = preprocess_image(image_path)
    prediction = model.predict(img)
    if prediction > 0.5:
        print("Crack Detected! 🚨")
    else:
        print("No Crack Detected ✅")

# Test with an image
detect_crack("pipeline_image.jpg")

