import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras

df = pd.read_csv('train_set.csv')

# print(df.head())

properties = list(df.columns.values)
properties.remove('Action')

x = df[properties]

x = np.asarray(x).astype('float32')

y = df['Action']

# print(x.head())
# print(y.head())

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(14-1,)),
    keras.layers.Dense(250, activation=tf.nn.relu),
	keras.layers.Dense(250, activation=tf.nn.relu),
    keras.layers.Dense(1, activation=tf.nn.sigmoid),
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=50, batch_size=1)
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)