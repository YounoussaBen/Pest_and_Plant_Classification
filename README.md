# Plant Disease Classifier and Pest Classifier

## Summary of Plant Disease Classifier

### Model Architecture
- Model Name: Sequential
- Total Parameters: 3,600,294
- Trainable Parameters: 3,597,414
- Non-trainable Parameters: 2,880
- Input Shape: 64x64 pixels with 3 color channels (RGB)
- Output Shape: 38 classes

### Model Description
The Plant Disease Classifier is a convolutional neural network (CNN) designed to identify various plant diseases based on input images of plant leaves. It consists of multiple layers, including convolutional layers, activation functions, batch normalization, max-pooling, and dropout layers. The final layer is a dense layer with 38 output classes, each representing a different plant disease or a healthy plant.

## Summary of Pest Classifier

### Model Architecture
- Model Name: Sequential
- Total Parameters: 17,861,873
- Trainable Parameters: 184,246
- Non-trainable Parameters: 17,677,627
- Input Shape: Variable (Dependent on the mobileNetV2 model)
- Output Shape: 12 classes

### Model Description
The Pest Classifier is designed to identify various pests based on input images. It uses the mobileNetV2 model as a feature extractor, followed by batch normalization and dense layers for classification. This model has 12 output classes, each representing a different type of pest.

## Usage
Both models can be used for image classification tasks by providing an image as input to the respective model. The models will output a class label indicating the predicted disease (for the Plant Disease Classifier) or pest type (for the Pest Classifier).

## Dependencies
- Python 3.x
- TensorFlow
- Other required Python packages (see the project's requirements.txt file)

## Credits
The Plant Disease Classifier and Pest Classifier models were trained and developed as part of the CropScan mobile app, a collaborative effort by Ben and Raymond for their capstone project. CropScan is dedicated to plant and pest disease detection using deep learning techniques.

In addition, we acknowledge the following contributors and their work:

- Akshay224 for the creation and maintenance of the PlantVillage dataset, which provided crucial data for training the Plant Disease Classifier.

- Vencerlanz09 for their dedicated work on the dataset Agricultural Pests Image Dataset, which played a significant role in the development of the Pest Classifier.

- Vencerlanz09's contribution to the development of the EfficientNetV2-L model was instrumental in fine-tuning the Pest Classifier to effectively detect and classify pests in agricultural settings.

- Pavan-Turlapati's work on the Plant Disease Detection and Identification project served as a valuable reference and inspiration for the development of the Plant Disease Classifier, providing insights into model architecture and training techniques.

We extend our sincere gratitude to these individuals and their contributions, which have greatly contributed to the success of the CropScan app and its mission of plant and pest disease detection.

## License
This project is licensed under the MIT License.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
