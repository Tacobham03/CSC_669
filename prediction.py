from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras import models

test_folder_path = "C:\\Users\\Libby\\Documents\\DNN\\images"

test_datagen = ImageDataGenerator(rescale=1./255)

validation_generator = test_datagen.flow_from_directory(
	test_folder_path,
	target_size=(48, 48),
	batch_size=128,
	color_mode='grayscale',
	class_mode='categorical')

predictions = model.predict_generator(generator=validation_generator)
y_pred = [np.argmax(probas) for probas in predictions]
y_test = validation_generator.classes
class_names = list(validation_generator.class_indices.keys())

# Generate confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Plot confusion matrix
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(cm, cmap='PuBuGn')
ax.grid(False)
ax.set_xlabel('Predicted labels', fontsize=12, color='black')
ax.set_ylabel('True labels', fontsize=12, color='black')
ax.set_xticks(np.arange(len(class_names)))
ax.set_yticks(np.arange(len(class_names)))
ax.set_xticklabels(class_names, fontsize=10, color='black')
ax.set_yticklabels(class_names, fontsize=10, color='black')
for i in range(len(class_names)):
	for j in range(len(class_names)):
		ax.text(j, i, cm[i, j], ha='center', va='center', color='black')

plt.show()