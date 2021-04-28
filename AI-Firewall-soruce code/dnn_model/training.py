import pandas as pd
import numpy as py
import csv
import time
import shutil

import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping

early_stopping_monitor = EarlyStopping(patience=10)

def build_model(train_x, train_y, shape, csv_name, number):
    
    begin = time.time()
    
    node_layer_1 = 40
    node_layer_2 = 40
    node_layer_3 = 40
    epoch = 30
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
    
    train_time = time.time() - begin
    
    model_name = 'model_' + str(number)
    
    model.save(model_name + '.h5')
    
    shutil.move(model_name + '.h5', "_model/" + model_name + '.h5')
    
    result(train_time, score, acc, csv_name, model_name)
    
def train_model():
    number_set = len(pd.read_csv('_csv/data_info.csv'))
    
    if number_set == 0:
        print('training: no train_set found')

    for i in range(number_set):
        
        file_name = '_csv/train_set/train_' + str(i+1)
        
        data = pd.read_csv(file_name + '.csv')
        
        train_x = data.iloc[:,1:data.shape[1]].values
        train_y = data.iloc[:,0].values
        
        train_x = train_x.astype('float32')

        shape = data.shape[1] - 1
        
        build_model(train_x, train_y, shape, file_name, i+1)
        
def result(train_time, score, acc, csv_name, model_name):
    with open("_csv/result/training_result.csv", 'a', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([csv_name[15:], model_name, train_time, acc, score])