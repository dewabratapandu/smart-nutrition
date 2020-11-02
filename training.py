import tensorflow as tf
import keras
from keras import layers, optimizers
from keras.models import Model
from keras.layers import Dense, Activation, Flatten, Conv2D, MaxPool2D, AveragePooling2D, BatchNormalization, \
    ZeroPadding2D, Input, GlobalAveragePooling2D
import numpy as np
import cv2
import os

x_train = []; y_train = []
for filename in os.listdir("datasets/train"):
    im = cv2.imread(os.path.join("datasets/train", filename), 1)
    im = cv2.resize(im, (224, 224))
    x_train.append(im)
    if(filename[0] == '0'):
        y_train.append(0)
    elif(filename[0] == '1'):
        y_train.append(1)
    elif(filename[0] == '2'):
        y_train.append(2)
    elif(filename[0] == '4'):
        y_train.append(3)

x_test = []; y_test = []
for filename in os.listdir("datasets/test"):
    im = cv2.imread(os.path.join("datasets/test", filename), 1)
    im = cv2.resize(im, (224, 224))
    x_test.append(im)
    if(filename[0] == '0'):
        y_test.append(0)
    elif(filename[0] == '1'):
        y_test.append(1)
    elif(filename[0] == '2'):
        y_test.append(2)
    elif(filename[0] == '4'):
        y_test.append(3)

x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
print(x_train.shape)
# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, 4)
y_test = keras.utils.to_categorical(y_test, 4)
print(y_train.shape)

#################

base_model = keras.applications.MobileNetV2(weights='imagenet', include_top=False)
x = base_model.output
x = GlobalAveragePooling2D()(x)
predictions = Dense(4, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=predictions)
model.summary()

adam = optimizers.Adam(0.001)
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=adam,
              metrics=['accuracy'])
cb = keras.callbacks.ModelCheckpoint("./models/model.hdf5", monitor='loss',
                                            verbose=1, save_best_only=True,
                                            save_weights_only=False, mode='auto', period=1)
callback = [cb]
model.fit(x_train, y_train,
          batch_size=16,
          epochs=1500,
          verbose=1,
          validation_data=(x_test, y_test),
          callbacks=callback)

# evaluating and printing results
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])