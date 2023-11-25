import tensorflow as tf
from keras import layers, models
from keras.preprocessing.image import ImageDataGenerator

# Model definition (unchanged)

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # 1 output node for binary classification (cat or dog)
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Data augmentation and loading (unchanged)

train_datagen = ImageDataGenerator(rescale=1./255,
                                   rotation_range=20,
                                   width_shift_range=0.2,
                                   height_shift_range=0.2,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True,
                                   fill_mode='nearest')

# Adjust the path to your dataset
train_directory = './train'
print(f"Checking the content of directory: {train_directory}")
import os
print(os.listdir(train_directory))

# Adjust the path to your dataset
train_generator = train_datagen.flow_from_directory(
    train_directory,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

history = model.fit(train_generator, epochs=20)

# Save the entire model to a file
model.save('my_model_20.keras')
