import os
import tempfile
from PIL import Image
import gradio as gr
import tensorflow as tf
import cv2

# Replace these variables with your model and class names
model_path = 'models/pest_detector.h5'
class_names = ["ants", "bees", "beetle", "caterpillar", "earthworms", "earwig", "grasshopper",
              "moth", "slug", "snail", "wasp", "weevil"]

lenet_model = tf.keras.models.load_model(model_path)

def predicts(image_array):
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Define the file path for saving the image
    image_path = os.path.join(temp_dir, 'temp_image.jpg')  # Change the file format if needed

    # Save the image using OpenCV
    cv2.imwrite(image_path, image_array)
    test_img = Image.open(image_path)
    test_img = tf.image.resize(test_img, size=(256, 256))  # Update to match your model's input size
    im = tf.constant(test_img, dtype=tf.float32)
    im = tf.expand_dims(im, axis=0)
    
    prediction = lenet_model(im)
    predicted_class_index = tf.argmax(prediction, axis=-1).numpy()[0]
    predicted_class = class_names[predicted_class_index]
    
    # Get confidence score for the detected class
    confidence_score = prediction[0][predicted_class_index].numpy()
    
    return predicted_class.upper(), confidence_score

iface = gr.Interface(fn=predicts, inputs='image', outputs=['text', 'number'])
iface.launch(share=True)
