# -*- coding: utf-8 -*-
"""

Phase - 3 Evaluation and Compare Reference

Created on Tue Sep 30 19:30:27 2020

@author: POP PC (60070019) for TSIT Project 63

"""

# File Configuration

csv_file_input = "test_4rule_bin" # place the name of data here
csv_file_use = "%s.csv" % csv_file_input

name_model = "model_test" # place the name of model here
name_model_use = "%s.h5" % name_model

true_positive = 0
true_negative = 0
false_positive = 0
false_negative = 0

import pandas as pd
import numpy as np

data = pd.read_csv(csv_file_use)

test_x = data.iloc[:,1:data.shape[1]].values
test_y = data.iloc[:,0].values

import keras
from tensorflow.keras.models import load_model

model = load_model(name_model_use)

print("Evaluating . . . . . .")

import time
time_start = time.time()

# prediction = model.evaluate(test_x)
prediction = model.predict(test_x)

# Compare Reference

for i in range(len(prediction)):
    
    if round(prediction[i][0]) == int(test_y[i]):
        if round(prediction[i][0]) == 1:
            true_positive += 1
        elif round(prediction[i][0]) == 0:
            true_negative += 1
            
    elif round(prediction[i][0]) != int(test_y[i]):
        if round(prediction[i][0]) == 1:
            false_positive += 1
        elif round(prediction[i][0]) == 0:
            false_negative += 1

time_finish = time.time()
time_duration = time_finish - time_start

# Accuracy
test_accuracy = float(true_positive + true_negative) / len(prediction)
loss_rate = float(false_positive + false_negative) / len(prediction)

print("Number of Packet: ",len(prediction))
print("Compare Time: %.6f seconds" % time_duration)
print("Accuracy of testing: " + str(test_accuracy*100) + " %")
print("Loss rate: " + str(loss_rate*100) + " %")
print("TP:", true_positive, "TN:", true_negative, "FP:", false_positive, "FN:", false_negative)
