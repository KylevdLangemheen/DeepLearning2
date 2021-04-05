import os
import cv2
import random
import numpy as np

train_image = []
test_image = []

current_directory = os.path.dirname(os.path.realpath(__file__))
house_directory = current_directory + "/LegoHouse"

for filename in os.listdir(house_directory):
    if filename.endswith(".jpg"):
        img = cv2.imread(house_directory + "/" +filename)
        img_resized = cv2.resize(img,(256,256),interpolation = cv2.INTER_AREA)
        if random.random() < 0.8:
            train_image.append(img_resized)
        else:
            test_image.append(img_resized)

train_image = np.asarray(train_image)
test_image = np.asarray(test_image)

print (train_image.shape)
print (test_image.shape)

with open('train_lego.npy', 'wb') as f:
    np.save(f,train_image,allow_pickle= True)
with open('test_lego.npy', 'wb') as f:
    np.save(f,test_image, allow_pickle=True)