# read data input

import csv
import os
import shutil
import pandas as pd

def generate_template():
    header = []
    
    for i in range(1,37):
        header.append('rule_' + str(i))
        
    header.append('default')
    header.append('train_set_name')
    
    # print(header)
    
    with open('template.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        
    # move file to .. directory
    shutil.move("template.csv", "_csv/template.csv")

def read_csv():
    dataframe = []
    
    # if run only function don't forget ../
    with open('_csv/data_info.csv','rt') as f:
        data = csv.reader(f)
        next(data, None)  # skip the headers
        
        for row in data:
            dataframe.append(row)
        
    return dataframe

def generate_field(): # for train set only
    dataframe = [1,4,4,6,2,4,1,32,16,32,16,8]
    column = []
    count = 1
    for i in dataframe:
        for j in range(i):
            column.append(str(count)+'_'+str(j+1))
        count += 1
    return column

def generate_result():
    header = []
    header.append('file_name')
    header.append('total_packet')
    header.append('gen_time')
    
    with open('generate_result.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(header)
    shutil.move("generate_result.csv", "_csv/result/generate_result.csv")

def training_result():
    header = []
    header.append('file_name')
    header.append('model_name')
    header.append('train_time')
    header.append('train_accuracy')
    header.append('train_loss')
    
    with open('training_result.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(header)
    shutil.move("training_result.csv", "_csv/result/training_result.csv")
    
def evaluate_result():
    header = []
    header.append('model_name')
    header.append('evaluate_time')
    header.append('evaluate_accuracy')
    header.append('True_positive')
    header.append('True_negative')
    header.append('False_positive')
    header.append('False_positive')
    
    with open('evaluate_result.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(header)
    shutil.move("evaluate_result.csv", "_csv/result/evaluate_result.csv")
    
    