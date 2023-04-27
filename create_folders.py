import os
import random
import shutil

folder_path = "C:\\Users\\Tom\\Documents\\New Folder\\images"
train_folder_name = "C:\\Users\\Tom\\Documents\\New Folder\\train"
test_folder_name = "C:\\Users\\Tom\\Documents\\New Folder\\test"


for emotion_folder in os.listdir(folder_path):
    
    train_subfolder_path = os.path.join(train_folder_name, emotion_folder)
    test_subfolder_path = os.path.join(test_folder_name, emotion_folder)
    os.makedirs(train_subfolder_path, exist_ok=True)
    os.makedirs(test_subfolder_path, exist_ok=True)
   
    image_list = os.listdir(os.path.join(folder_path, emotion_folder))
    random.shuffle(image_list)
 
    train_size = int(len(image_list) * train_split)
    train_images = image_list[:train_size]
    test_images = image_list[train_size:]
    
    for image_name in train_images:
        source_path = os.path.join(folder_path, emotion_folder, image_name)
        destination_path = os.path.join(train_subfolder_path, image_name)
        shutil.copyfile(source_path, destination_path)

    for image_name in test_images:
        source_path = os.path.join(folder_path, emotion_folder, image_name)
        destination_path = os.path.join(test_subfolder_path, image_name)
        shutil.copyfile(source_path, destination_path)

print("Train and test folders created successfully!")
