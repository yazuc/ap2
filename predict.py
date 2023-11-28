import numpy as np
from keras.preprocessing import image
from keras.models import load_model
import pandas as pd
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load the trained model
model_5  = load_model('./my_model_5.h5')
model_10 = load_model('./my_model_10.h5')
model_20 = load_model('./my_model_20.h5')

# Load and preprocess the image you want to predict
img_path_cat = './test/cat'
img_path_dog = './test/dog'

# List Test Images
cat_images = pd.DataFrame(os.listdir(img_path_cat), columns=['Files'])
cat_images['TargetValue'] = 'cat'
dog_images = pd.DataFrame(os.listdir(img_path_dog), columns=['Files'])
dog_images['TargetValue'] = 'dog'
images = pd.concat([cat_images, dog_images], ignore_index=True)
images['Prediction_5'] = ""
images['Prediction_10'] = ""
images['Prediction_20'] = ""

# Predict Images for each Model
for index, row in images.iterrows():
    print(index)
    img = image.load_img(os.path.join('./test', images.iloc[index]["TargetValue"], images.iloc[index]["Files"]), target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the pixel values to be between 0 and 1

    # Make predictions
    prediction_5 = model_5.predict(img_array)
    prediction_10 = model_10.predict(img_array)
    prediction_20 = model_20.predict(img_array)

    if prediction_5 > 0.5:
        images.at[index,'Prediction_5'] = "dog"
    else:
        images.at[index,'Prediction_5'] = "cat"

    if prediction_10 > 0.5:
        images.at[index,'Prediction_10'] = "dog"
    else:
        images.at[index,'Prediction_10'] = "cat"

    if prediction_20 > 0.5:
        images.at[index,'Prediction_20'] = "dog"
    else:
        images.at[index,'Prediction_20'] = "cat"

images.to_excel('forecastings_v2.xlsx', index=False)
