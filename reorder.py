import os
import shutil

# Adjust the path to your dataset
dataset_path = 'C:/Users/Leonardo/Downloads/ap2/train'

# Create subdirectories if they don't exist
for class_name in ['cat', 'dog']:
    class_path = os.path.join(dataset_path, class_name)
    os.makedirs(class_path, exist_ok=True)

# Move files to the appropriate subdirectories
for filename in os.listdir(dataset_path):
    if 'cat' in filename:
        src_path = os.path.join(dataset_path, filename)
        dest_path = os.path.join(dataset_path, 'cat', filename)
        if not os.path.isdir(src_path):  # Check if it's not a directory
            shutil.move(src_path, dest_path)
    elif 'dog' in filename:
        src_path = os.path.join(dataset_path, filename)
        dest_path = os.path.join(dataset_path, 'dog', filename)
        if not os.path.isdir(src_path):  # Check if it's not a directory
            shutil.move(src_path, dest_path)
