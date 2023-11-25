import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image
from keras.models import load_model
import os

from PIL import Image
import matplotlib.pyplot as plt

import pandas as pd

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load the trained model
model_10 = load_model('C:\\Users\\Leonardo\\Downloads\\ap2\\my_model_10.keras')

# Load and preprocess the image you want to predict
img_path = 'C:\\Users\\Leonardo\\Downloads\\ap2\\miguel.jpg'  # Change this to the path of the image you want to predict

# Create a DataFrame for the single image
images = pd.DataFrame({'Files': [os.path.basename(img_path)],
                       'TargetValue': 'cat'})  # Assuming the image is a cat, change it accordingly
images['Prediction_10'] = ""

# Predict Image for the Model
index = 0  # Since there's only one image, set index to 0
img = image.load_img(img_path, target_size=(150, 150))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0  # Normalize the pixel values to be between 0 and 1

# Make predictions
prediction_10 = model_10.predict(img_array)

# Create a subplot for image and bar chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

imgbestquality = Image.open(img_path)

# Display the image
ax1.imshow(imgbestquality)
ax1.axis('off')

# Display the prediction results in the second subplot
predicted_class = "dog" if prediction_10 > 0.5 else "cat"
confidence_score = max(prediction_10[0][0], 1 - prediction_10[0][0])

ax2.bar(['Cat', 'Dog'], [1 - prediction_10[0][0], prediction_10[0][0]], color=['blue', 'orange'])
ax2.set_ylabel('Probability')
ax2.set_title(f'Prediction: {predicted_class}\nConfidence Score: {confidence_score:.2f}')

plt.show()
