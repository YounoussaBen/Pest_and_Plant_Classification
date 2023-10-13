import streamlit as st
import tensorflow as tf
import numpy as np
import cv2

# Load your saved Keras model
model = tf.keras.models.load_model('/home/skay/Documents/Project/Capstone/pest-and-plant-classification/models/plant_disease_classifier.h5')

label_list = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight',
    'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight',
    'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
]

default_image_size = (64, 64)

def convert_image_to_array(image_file):
    try:
        image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
        if image is not None:
            image = cv2.resize(image, default_image_size)
            return image
        else:
            return np.array([])
    except Exception as e:
        print("Error:", e)
        return None

def classify_plant_disease(image):
    # Normalize the image
    image = np.array(image, dtype=np.float16) / 255.0

    # Expand dimensions to match the model's input shape
    image = np.expand_dims(image, axis=0)

    # Testing the model
    results = model.predict(image)

    # Determine the predicted class index
    predicted_class_index = np.argmax(results)
    predicted_label = label_list[predicted_class_index]

    # Get confidence score for the detected class
    confidence_score = results[0][predicted_class_index]

    return predicted_label, confidence_score

# Streamlit app
st.title("Plant Disease Classification")

# Upload an image for classification
uploaded_image = st.file_uploader("Upload an image of a plant", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = convert_image_to_array(uploaded_image)

    if image is not None:
        st.image(image, caption="Uploaded Image", use_column_width=True)
        predicted_label, confidence_score = classify_plant_disease(image)
        st.write(f"Predicted Label: {predicted_label}")
        st.write(f"Confidence Score: {confidence_score:.4f}")
