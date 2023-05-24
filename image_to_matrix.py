# This file converts image into np.array

import os
from PIL import Image
import numpy as np


X = []
y = []

base_path='/home/archangel7431/internship/images'
for child in os.listdir(base_path):
  for data_file in os.listdir(base_path):
    X_i = Image.open(os.path.join(base_path, data_file)).convert('L')
    X_i = np.array(X_i.resize((120,120))) / 255.0
    X.append(X_i)
   
print(X)

X = np.array(X)
print(X.shape)