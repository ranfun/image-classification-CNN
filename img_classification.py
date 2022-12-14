# -*- coding: utf-8 -*-
"""assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vt0Q1XF3iWwDWOLQUf-5f44_5dNzXfAr
"""

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

np.shape(train_images[0])

print(train_images[0].T)

np.shape(test_images)

np.shape(train_images)

def image_show(imagedata,labeldata,j):
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer','dog', 'frog', 'horse', 'ship', 'truck']
    plt.figure(figsize=(10,10))
    x = np.squeeze(labeldata)
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(imagedata[i+j], cmap=plt.cm.binary)
        plt.xlabel(class_names[x[i+j]])
    plt.show()

train_images, test_images = train_images / 255.0, test_images / 255.0

train_labels, test_labels = train_labels.flatten(), test_labels.flatten()

image_show(train_images,train_labels,0)

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3),padding='same'))
model.add(layers.BatchNormalization())
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu',padding='same'))
model.add(layers.BatchNormalization())
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu',padding='same'))
model.add(layers.BatchNormalization())
model.add(layers.Flatten())
model.add(layers.Dropout(0.2))
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(10, activation='softmax'))
model.summary()

model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),  metrics=['accuracy'])

model.fit(train_images, train_labels,validation_data=(test_images, test_labels), epochs=10)

validation_data=(test_images, test_labels)

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

