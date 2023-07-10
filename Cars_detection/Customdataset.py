"""
This Class creates a custom dataset that will define images fit to their bounding boxes

and split dataset into train validation for training.
  
 """
 
 class CustomDataset(Dataset):
    def __init__(self, image_dir, dataframe):
        self.image_dir = image_dir
        self.dataframe = dataframe

        # Filter out images without bounding boxes
        image_with_bboxes = set(self.dataframe['image'])
        self.image_paths = [os.path.join(self.image_dir, image_name)
                            for image_name in os.listdir(self.image_dir)
                            if image_name in image_with_bboxes]

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image_path = self.image_paths[idx]
        image = Image.open(image_path).convert("RGB")

        # Retrieve bounding box information from the dataframe based on image path
        image_name = os.path.basename(image_path)
        bbox_row = self.dataframe[self.dataframe['image'] == image_name].iloc[0]
        x_center = bbox_row['x_center']
        y_center = bbox_row['y_center']
        height = bbox_row['height']
        width = bbox_row['width']

        return image, (x_center, y_center, height, width)
image_dir = '/kaggle/input/car-object-detection/data/training_images'

dtset = CustomDataset(image_dir, new_df)
len(dtset)  
    
    
# split the dataset

train_len = int(len(dtset) * 0.8)
val_len = len(dtset) - train_len
train_set, val_set = random_split(dtset, [train_len, val_len])

batch_size = 64
train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_set, batch_size=batch_size, shuffle=False)
print(f'Train:{len(train_set)}')
print(f'Validation:{len(val_set)}')   

#Train:284
#Validation:71
