# -*- coding: utf-8 -*-
"""

Phase - 2 Trainin Model

Created on Tue Sep 16 09:57:31 2020

@author: POP PC (60070019) for TSIT Project 63

"""

# 1 insert local variable here

# File Configuration
csv_file_input = "train_set" # place the name of data here
csv_file_use = "%s.csv" % csv_file_input

# Model Configuration
node_layer_1 = 150
node_layer_2 = 150
node_layer_3 = 150
epoch = 10

name_model = "model_test" # place the name of model here
name_model_use = "%s.h5" % name_model

# 2 pull the data in

import pandas as pd
import numpy as py

data = pd.read_csv(csv_file_use)

# shuffle data

data = data.sample(frac=1)

train_x = data.iloc[:,1:data.shape[1]].values
train_y = data.iloc[:,0].values

# data processing

train_x = train_x.astype('float32')

import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping

#

early_stopping_monitor = EarlyStopping(patience=10)

print('building model....')

model = Sequential()

model.add(Dense(node_layer_1, activation='relu', input_shape = (data.shape[1]-1,)))
model.add(Dense(node_layer_2, activation='relu'))
model.add(Dense(node_layer_3, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer="Adam", loss='binary_crossentropy', metrics=['accuracy'])

data2 = data.shape

# Start count training time

import time

print("Training . . . . . .")

begin = time.time()

# Training phase

model.fit(train_x, train_y, epochs = epoch, batch_size = 32)

# End count training time

end = time.time()

# Do summary of training

model.summary()

score, acc = model.evaluate(train_x, train_y)

print('Score:', score)
print('Accuracy:', acc*100, '%')

print('Saving Model..', name_model_use)
print('(', "%.4f" % (end-begin), 'seconds'+ ' )')

model.save(name_model_use)