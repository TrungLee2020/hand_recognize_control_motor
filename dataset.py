import numpy as np
import os
import cv2
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg  # Plotting
from tqdm import tqdm
import csv


def Create_Directory_DataFrame():
    df = pd.DataFrame(columns=['Class', 'Location'])
    basedir = 'data/leapgestrecog/'
    for folder in os.listdir(basedir):
        for Class in os.listdir(basedir + folder + '/'):
            for location in os.listdir(basedir + folder + '/' + Class + '/'):
                df = df.append({'Class': Class, 'Location': basedir + folder + '/' + Class + '/' + location},
                               ignore_index=True)
    df = df.sample(frac=1)
    return df


if __name__ == '__main__':
    df = Create_Directory_DataFrame()
    # print(df.shape)
    print(df.head())
    # count = 1
    # f = plt.figure(figsize=(50, 13))
    # for Class in df['Class'].unique():
    #     seg = df[df['Class'] == Class]
    #     address = seg.sample().iloc[0]['Location']
    #     img = cv2.imread(address, 0)
    #     ax = f.add_subplot(2, 5, count)
    #     ax = plt.imshow(img)
    #     ax = plt.title(Class, fontsize=30)
    #     count = count + 1
    # plt.suptitle("Hand Sign Images", size=32)
    # plt.show()
    w, h = 64, 64
    final_class = 10
    train_image = []
    for location in tqdm(df.iloc[:]['Location']):
        img = cv2.imread(location, 0)
        img = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
        img = img.reshape(w, h, 1)
        train_image.append(img)
    X = np.array(train_image)
