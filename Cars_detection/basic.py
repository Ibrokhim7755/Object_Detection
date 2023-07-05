"""

This file involves the basic requirements of my project including required libraries,
loading the images and csv file of annotations, then visualizing them to check whether they fit
to each other, and finally checking shape of widths and heights of image dataset.
  
"""

import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os, cv2, yaml
from tqdm import tqdm
from PIL import Image
from collections import defaultdict
from glob import glob
from torch.utils.data import DataLoader, Dataset, random_split
from torchvision.datasets import ImageFolder

df = pd.read_csv('D:/Data/Datasets/cars_detection/train_solution_bounding_boxes (1).csv')
df.head()


'''
This is visualizing code 
'''

im_path = 'D:/Data/Datasets/cars_detection/training_images/'

for i in df.index:

    img = Image.open(im_path + str(df['image'][i]))
    x_min = df['xmin'][i]
    y_min = df['ymin'][i]
    width = (df['xmax'][i] - df['xmin'][i])
    height = (df['ymax'][i] - df['ymin'][i])
    fig, ax = plt.subplots()
    rectangle = patches.Rectangle((x_min,y_min), width,height, linewidth=1, edgecolor='g',facecolor='none')
    ax.imshow(img)
    ax.add_patch(rectangle)
    plt.show()
    if i == 10:
        break
    
    
    # checking height and widths
    
    for i in df.index:
    img = cv2.imread(im_path + str(df['image'][i]))
    print(img.shape)
    if i == 10:
        break