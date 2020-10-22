"""this is model for AI Training"""

import pandas as pd


#import csv data
data = pd.read_csv('nba_logreg.csv')

# exception for empty cell
data.drop("3P%", axis=1, inplace=True)
data.isnull().any()

#try select the row with .iloc ---- This is Data Information Field to only 19 bcz 20 is answer
x = data.iloc[:,1:19].values

#try select the row with .iloc ---- This is Answer of Data might be 0 or 1
y = data.iloc[:,19].values

#spiliting data to training set or test set // because there's only 1 file so we spilt one for tutoriral
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=0)

#feature scailing
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Build Node and Hidden Layer
import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential ()

model.add(Dense(units = 10, kernel_initializer = 'uniform', activation='relu',input_dim = 18))
model.add(Dense(units = 10, kernel_initializer = 'uniform', activation='relu'))
model.add(Dense(units = 1, kernel_initializer = 'uniform', activation='relu'))
model.compile(optimizer = 'adam',loss = 'binary_crossentropy', metrics = ['accuracy'])

#count training time and after -- this is start to count time
import time
time_start = time.time()

# Build Training Phase
model.fit(x_train,y_train,batch_size = 10, epochs =100)

#count training time and after - 2 -- this is after finished training
time_finish = time.time()
time_duration = time_finish - time_start
print("time_used: " + str(time_duration) + " seconds")

# predict
# y_pred = model.predict(x_test)
# print(y_pred)
model.summary()
score, acc = model.evaluate(x_train, y_train)
print('Test score:', score)
print('Test accuracy:', acc)

model.save('model.h5')