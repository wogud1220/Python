import tensorflow as tf
import keras
import numpy as np

mist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mist.load_data()

print(x_train[:5])