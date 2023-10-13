import tensorflow as tf

# model_path = 'models/plant_disease_classifier.h5'  
model_path = 'models/models/pest_detector.h5'  # Provide the correct path to your model file

# Load the model
model = tf.keras.models.load_model(model_path)

# Display the model summary
model.summary()

