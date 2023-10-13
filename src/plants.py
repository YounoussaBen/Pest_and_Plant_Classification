import tensorflow as tf
import numpy as np
import cv2

# Load your saved Keras model
model = tf.keras.models.load_model('models/plant_disease_classifier.h5')

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

def convert_image_to_array(image_dir):
    try:
        image = cv2.imread(image_dir)
        if image is not None:
            image = cv2.resize(image, default_image_size)
            return image
        else:
            return np.array([])
    except Exception as e:
        print("Error:", e)
        return None

# IMAGE PRE-PROCESSING

img = convert_image_to_array('images/plants/Cherry/Healthy/6f7e749d-006a-47a8-94d0-66292e2279fb___JR_HL 9722.JPG')

# Normalize the image
img = np.array(img, dtype=np.float16) / 255.0

# Expand dimensions to match the model's input shape
img = np.expand_dims(img, axis=0)

# TESTING THE MODEL HERE
results = model.predict(img)

# Determine the predicted class index
predicted_class_index = np.argmax(results)
predicted_label = label_list[predicted_class_index]

# Get confidence scores for all classes
# confidence_scores = results[0]  # Assuming you have only one prediction

# Get confidence score for the detected class
confidence_score = results[0][predicted_class_index]

# Print the predicted label and confidence scores
print("Predicted Label:", predicted_label)
print("Confidence Score for Detected Class:", confidence_score)

# print("Confidence Scores:")
# for label, score in zip(label_list, confidence_scores):
#     print(f"{label}: {score:.4f}")
