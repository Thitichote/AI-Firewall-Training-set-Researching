import csv
import pandas as pd
import keras

from tensorflow.keras.models import load_model

import time

def evaluate_model():

    number_set = len(pd.read_csv('_csv/data_info.csv'))
    
    # put up test set
    data = pd.read_csv('_csv/test_set/test_set.csv')
    
    test_x = data.iloc[:,1:data.shape[1]].values
    test_y = data.iloc[:,0].values
    
    for i in range(number_set):
        
        begin = time.time()
        
        true_positive = 0
        true_negative = 0
        false_positive = 0
        false_negative = 0
        
        model_name = 'model_' + str(i+1)
        
        model = load_model('_model/' + model_name + '.h5')
        
        print("Evaluating ... " + model_name + '.h5')
        
        prediction = model.predict(test_x)
        
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
        
        evaluate_time = time.time() - begin
        
        accuracy = (float(true_positive + true_negative) / len(prediction)) * 100
        false_accuracy = float(false_positive + false_negative) / len(prediction)
        
        with open("_csv/result/evaluate_result.csv", 'a', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow([model_name, evaluate_time, accuracy, true_positive, true_negative, false_positive, false_negative])
    
    print('done..')