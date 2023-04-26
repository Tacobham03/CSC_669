def create_train_test_folders(folder_path, train_folder_name, test_folder_name, train_split=0.7):

    for emotion_folder in os.listdir(folder_path):
        
        # Create train and test subfolders for each emotion folder
        train_subfolder_path = os.path.join(train_folder_name, emotion_folder)
        test_subfolder_path = os.path.join(test_folder_name, emotion_folder)
        os.makedirs(train_subfolder_path, exist_ok=True)
        os.makedirs(test_subfolder_path, exist_ok=True)

        # Get list of images in the current emotion folder
        image_list = os.listdir(os.path.join(folder_path, emotion_folder))
        random.shuffle(image_list)

        # Split the images into training and testing sets
        train_size = int(len(image_list) * train_split)
        train_images = image_list[:train_size]
        test_images = image_list[train_size:]

        # Move the training images to the train subfolder
        for image_name in train_images:
            source_path = os.path.join(folder_path, emotion_folder, image_name)
            destination_path = os.path.join(train_subfolder_path, image_name)
            shutil.copyfile(source_path, destination_path)

        # Move the testing images to the test subfolder
        for image_name in test_images:
            source_path = os.path.join(folder_path, emotion_folder, image_name)
            destination_path = os.path.join(test_subfolder_path, image_name)
            shutil.copyfile(source_path, destination_path)

    print("Train and test folders created successfully!")
