# read data input

import csv
import os
import shutil
import pandas as pd

def generate_template():
    header = []
    
    for i in range(1,22):
        header.append('rule_' + str(i))
        
    header.append('default')
    header.append('train_set_name')
    
    # print(header)
    
    with open('template.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        
    # move file to .. directory
    shutil.move("template.csv", "template.csv")

def read_csv():
    dataframe = []
    
    # if run only function don't forget ../
    with open('data_info.csv','rt') as f:
        data = csv.reader(f)
        next(data, None)  # skip the headers
        
        for row in data:
            dataframe.append(row)
        
    return dataframe

def generate_field():
    dataframe = [1,4,4,6,2,4,1,32,16,32,16,8]
    column = []
    count = 1
    for i in dataframe:
        for j in range(i):
            column.append(str(count)+'_'+str(j+1))
        count += 1
    return column