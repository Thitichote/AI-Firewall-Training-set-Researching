import pandas as pd

import tensorflow as tf
from tensorflow import keras

df = pd.read_csv('Book1.csv')

print(df.head())

properties = list(df.columns.values)
properties.remove('head3')

x = df[properties]
y = df['1']

print(x.head())
print(y.head())

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1, random_state=0)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(14-1,)),
    keras.layers.Dense(16, activation=tf.nn.relu),
	keras.layers.Dense(16, activation=tf.nn.relu),
    keras.layers.Dense(1, activation=tf.nn.sigmoid),
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=50, batch_size=1)
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)