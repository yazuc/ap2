import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('my_model.h5')  # Replace with the path to your saved model

# Load and preprocess the image you want to predict
img_path = 'C:/Users/Leonardo/Downloads/ap2/dog.jpg'
img = image.load_img(img_path, target_size=(150, 150))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0  # Normalize the pixel values to be between 0 and 1

# Make predictions
predictions = model.predict(img_array)

# The model.predict() function returns the probability of the image belonging to class 1 (dog).
# You can interpret the result based on your binary classification task.

if predictions[0][0] > 0.5:
    print("It's a dog!")
else:
    print("It's a cat!")

