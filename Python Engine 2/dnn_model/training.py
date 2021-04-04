import pandas as pd
import numpy as py
import csv

import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping

early_stopping_monitor = EarlyStopping(patience=10)

def build_model(train_x, train_y, shape, number):
    
    node_layer_1 = 150
    node_layer_2 = 150
    node_layer_3 = 150
    epoch = 10
    batch = 32
    
    model = Sequential()

    model.add(Dense(node_layer_1, activation='relu', input_shape = (shape,)))
    model.add(Dense(node_layer_2, activation='relu'))
    model.add(Dense(node_layer_3, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer="Adam", loss='binary_crossentropy', metrics=['accuracy'])
    
    model.fit(train_x, train_y, epochs = epoch, batch_size = batch)
    
    model.summary()

    score, acc = model.evaluate(train_x, train_y)
    
    model.save('model_' + str(number) + '.h5')
    
def training():
    number_set = len(pd.read_csv('data_info.csv'))

    for i in range(number_set):
        
        data = pd.read_csv('train_' + str(i+1) + '.csv')
        
        train_x = data.iloc[:,1:data.shape[1]].values
        train_y = data.iloc[:,0].values
        
        train_x = train_x.astype('float32')

        shape = data.shape[1] - 1
        
        build_model(train_x, train_y, shape, i+1)

training()