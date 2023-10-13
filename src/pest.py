from PIL import Image
import tensorflow as tf

model_path = 'models/pest_detector.h5'  # Provide the correct path to your trained model file
class_names = ["ants", "bees", "beetle", "caterpillar", "earthworms", "earwig", "grasshopper",
              "moth", "slug", "snail", "wasp", "weevil"]

lenet_model = tf.keras.models.load_model(model_path)

def predict_from_image_path(image_path):
    try:
        # Load and preprocess the image
        test_img = Image.open(image_path)
        test_img = test_img.resize((256, 256))  # Update to match your model's input size
        im = tf.constant(test_img, dtype=tf.float32)
        im = tf.expand_dims(im, axis=0)

        # Make a prediction
        prediction = lenet_model(im)
        predicted_class_index = tf.argmax(prediction, axis=-1).numpy()[0]
        predicted_class = class_names[predicted_class_index]

        # Get confidence score for the detected class
        confidence_score = prediction[0][predicted_class_index]

        return predicted_class.upper(), confidence_score
    except Exception as e:
        return str(e)

# Example usage:
image_path = 'images/pests/ants/ants (9).jpg'  # Replace with the path to your image
result, confidence_score = predict_from_image_path(image_path)
print("Predicted class:", result)
print("Confidence Score for Detected Class:", confidence_score.numpy())
