import pandas as pd
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np

# Assuming your Excel file is named 'predictions.xlsx' and is in the same directory as your script
excel_file_path = './forecastings_v2.xlsx'

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file_path)

# Map string labels to numerical labels
label_mapping = {'cat': 0, 'dog': 1}
df['TargetValue'] = df['TargetValue'].map(label_mapping)
df['Prediction_5'] = df['Prediction_5'].map(label_mapping)
df['Prediction_10'] = df['Prediction_10'].map(label_mapping)
df['Prediction_20'] = df['Prediction_20'].map(label_mapping)

# Get true labels and predictions for each model
true_labels = df['TargetValue']
model1_preds = df['Prediction_5']
model2_preds = df['Prediction_10']
model3_preds = df['Prediction_20']

# Calculate confusion matrices
conf_matrix_model1 = confusion_matrix(true_labels, model1_preds)
conf_matrix_model2 = confusion_matrix(true_labels, model2_preds)
conf_matrix_model3 = confusion_matrix(true_labels, model3_preds)

# Create ConfusionMatrixDisplay objects
disp_model1 = ConfusionMatrixDisplay(conf_matrix_model1, display_labels=['cat', 'dog'])
disp_model2 = ConfusionMatrixDisplay(conf_matrix_model2, display_labels=['cat', 'dog'])
disp_model3 = ConfusionMatrixDisplay(conf_matrix_model3, display_labels=['cat', 'dog'])

# Create a subplot with 1 row and 4 columns
fig, axes = plt.subplots(1, 4, figsize=(20, 5))

# Plot confusion matrices
disp_model1.plot(ax=axes[0], cmap='Blues', values_format='d')
disp_model2.plot(ax=axes[1], cmap='Blues', values_format='d')
disp_model3.plot(ax=axes[2], cmap='Blues', values_format='d')

# Save confusion matrices for each model as separate images
plt.figure(figsize=(8, 6))
disp_model1.plot(cmap='Blues', values_format='d')
plt.title('Model 5 Epoch')
plt.savefig('confusion_matrix_model5.png')
plt.close()

plt.figure(figsize=(8, 6))
disp_model2.plot(cmap='Blues', values_format='d')
plt.title('Model 10 Epoch')
plt.savefig('confusion_matrix_model10.png')
plt.close()

plt.figure(figsize=(8, 6))
disp_model3.plot(cmap='Blues', values_format='d')
plt.title('Model 20 Epoch')
plt.savefig('confusion_matrix_model20.png')
plt.close()