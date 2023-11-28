import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image
from keras.models import load_model
import os

from PIL import Image
import matplotlib.pyplot as plt

import pandas as pd

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

my_model_10 = load_model("./my_model_10.h5")
my_model_20 = load_model("./my_model_20.h5")

acc_model1 = my_model_10.history['accuracy']

acc_model2 = my_model_20.history['accuracy']
