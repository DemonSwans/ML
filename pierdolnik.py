import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from time import sleep
import random

# Make NumPy printouts easier to read.
np.set_printoptions(precision=3, suppress=True)
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
print(tf.__version__)

column_names = ["Number1","znak" "Number2", "Number3"]
hash = tf.keras.layers.Hashing(2)
with open("liczby.txt",'r') as file:
   data=[]
   lines = file.readlines()
   for line in lines:
      line = line.replace("\n","").split(" ")
      line = [int(i) for i in line]
      data.append(line)
data = np.array(data)
data = pd.DataFrame(data,columns=["Number1","znak", "Number2", "Number3"])

train_dataset = data.sample(frac=0.8, random_state=0)
test_dataset = data.drop(train_dataset.index)

train_dataset.describe().transpose()

train_features = train_dataset.copy()
test_features = test_dataset.copy()

train_labels = train_features.pop('Number3')
test_labels = test_features.pop('Number3')

normalizer = tf.keras.layers.Normalization()

normalizer.adapt(np.array(train_features))
print(normalizer.mean.numpy())

first = np.array(train_features[:1])

with np.printoptions(precision=2, suppress=True):
  print('First example:', first)
  print()
  print('Normalized:', normalizer(first).numpy())

sum_normalizer = layers.Normalization(input_shape=[3,],axis=-1)
sum_normalizer.adapt(train_features)

sum_model = tf.keras.Sequential([
   sum_normalizer,
    layers.Dense(units=3),
layers.Dense(units=32,activation="sigmoid"),
layers.Dense(units=128, activation="sigmoid"),
layers.Dense(units=32),
layers.Dense(units=8),
   layers.Dense(units=1)
])

sum_model.summary()
sleep(3)
print(sum_model.predict(train_features[:10]))

sum_model.compile(
   optimizer=tf.optimizers.Adamax(learning_rate=0.001),
   loss="mean_absolute_error")

sum_model.fit(train_features,train_labels,epochs=80,validation_split = 0.2, batch_size= 1)
print("2-7")
print(2-7)
print(sum_model.predict([[2,0,7]])[0])
print("76+7")
print(76+7)
print(sum_model.predict([[76,1,17]])[0])
print("213-200")
print(213-200)
print(sum_model.predict([[213,0,200]])[0])
print("49+51")
print(49+51)
print(sum_model.predict([[49,1,51]])[0])
print("1231+3124")
print(1231+3124)
print(sum_model.predict([[1231,1,3124]])[0])
print("1-1111")
print(1-1111)
print(sum_model.predict([[1,0,1111]])[0])
print("12-3")
print(12-3)
print(sum_model.predict([[12,0,3]])[0])
