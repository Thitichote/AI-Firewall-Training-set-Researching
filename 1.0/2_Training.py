# -*- coding: utf-8 -*-
"""

Phase - 2 Trainin Model

Created on Tue Sep 16 09:57:31 2020

@author: POP PC (60070019) for TSIT Project 63

"""

# 1 insert local variable here

# File Configuration
csv_file_input = "train_binary" # place the name of data here
csv_file_use = "%s.csv" % csv_file_input

# Model Configuration
node_layer_1 = 150
node_layer_2 = 150
node_layer_3 = 150
epoch = 50

name_model = "model_test" # place the name of model here
name_model_use = "%s.h5" % name_model

# 2 pull the data in

import pandas as pd
import numpy as py

data = pd.read_csv(csv_file_use)

train_x = data.iloc[:,1:data.shape[1]].values
train_y = data.iloc[:,0].values

train_x = train_x.astype('float32')

import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from keras.optimizers import adam

model = Sequential()

model.add(Dense(node_layer_1, activation='relu', input_shape = (data.shape[1]-1,)))
model.add(Dense(node_layer_2, activation='relu'))
model.add(Dense(node_layer_3, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer="adam", loss='binary_crossentropy', metrics=['accuracy'])

# Start count training time

import time

print("Training . . . . . .")

time_start = time.time()

# Training phase

model.fit(train_x, train_y, epochs = epoch)

# End count training time

time_finish = time.time()
time_duration = time_finish - time_start

# Do summary of training

model.summary()

score, acc = model.evaluate(train_x, train_y)

print("Training time:", str(time_duration) + " Seconds")
print('Train score:', score)
print('Train accuracy:', acc)

model.save(name_model_use)
