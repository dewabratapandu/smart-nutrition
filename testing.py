import tensorflow as tf
import keras
from keras import layers, optimizers
from keras.models import Model
from keras.layers import Dense, Activation, Flatten, Conv2D, MaxPool2D, AveragePooling2D, BatchNormalization, \
    ZeroPadding2D, Input, GlobalAveragePooling2D
import numpy as np
import cv2
import os

model = keras.models.load_model('models/model.hdf5')

def testing(x):
    x = cv2.resize(x, (224, 224))
    x = x.astype("float32") / 255
    x = np.expand_dims(x, 0)

    y = model.predict(x)
    kelas = np.argmax(y[0])

    if kelas == 0:
        return 'Kosong'
    elif kelas == 1:
        return 'Nasi Goreng'
    elif kelas == 2:
        return 'Timun'
    elif kelas == 3:
        return 'Telur Dadar'

# a = testing('datasets/test/4_sisa025.jpg')
# print(a)