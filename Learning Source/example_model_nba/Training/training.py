"""this is model for AI Training"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import time

# Main Function
def main():
    #insert_input()
    learning_phase(10, 10, 10, 10, 20)

# Start Program config number of node and other
def insert_input():
    print("Example = Lnode1 Lnode2 batch_size epochs")
    print("Please Insert your input : ", end="")
    lNode1, lNode2, lNode3, sBatch, epoch = input().split(" ")
    print("Layer 1,2,3 =", str(lNode1), str(lNode2), str(lNode3))
    print("Batch size = " + str(sBatch) + " epoch = " + str(epoch))
    print("Type Y to next")
    if input() == "Y":
        learning_phase(lNode1, lNode2, lNode3, sBatch, epoch)
    else:
        print("try again!")
        insert_input()

# Learning Phase
def learning_phase(lNode1,lNode2,lNode3,sBatch,epo):
    
    # read csv
    data = pd.read_csv('nba_logreg.csv')

    # data drop reduce loss
    data.drop("3P%", axis=1, inplace=True)
    data.isnull().any()

    # x = data only
    raw_x = data.iloc[:,1:19].values

    # y = decision only
    raw_y = data.iloc[:,19].values

    # spilt data train
    x_train_split, x_test_split, y_train, y_test = train_test_split(raw_x, raw_y, test_size = 0.2, random_state = 10)

    # data preprocessing
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train_split)
    x_test = sc.transform(x_test_split)

    # create model
    model = Sequential ()
    model.add(Dense(units = lNode1, kernel_initializer = 'uniform', activation='relu',input_dim = 18))
    model.add(Dense(units = lNode2, kernel_initializer = 'uniform', activation='relu'))
    model.add(Dense(units = lNode3, kernel_initializer = 'uniform', activation='relu'))
    model.add(Dense(units = 1, kernel_initializer = 'uniform', activation='relu'))
    model.compile(optimizer = 'adam',loss = 'binary_crossentropy', metrics = ['accuracy'])

    # time count
    time_start = time.time()
    
    # start training 
    model.fit(x_train,y_train,batch_size = int(sBatch), epochs = int(epo))

    # finish time count
    time_finish = time.time()
    time_duration = time_finish - time_start

    print("TRAINING FINISHED!!\nSaving...")
    #if input() == "Y":
    #    evaluate()
    model.save("model.h5")
    time.sleep(3)
    
    
    model = load_model('model.h5')
    
    #model summary
    model.summary()
    score, acc = model.evaluate(x_train, y_train)
    
    prediction = model.predict(x_test)
    print(prediction.tolist()[0][0])
    print("Time used:", str(time_duration) + " seconds")
    print('Test score:', score)
    print('Test accuracy:', acc)

main()