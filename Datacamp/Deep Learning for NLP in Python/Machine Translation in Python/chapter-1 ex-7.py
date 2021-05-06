import tensorflow.keras as keras
import numpy as np
# Define an input layer
inp = keras.layers.Input(batch_shape=(2,3,4))
# Define a GRU layer that takes in the input
gru_out = keras.layers.GRU(10)(inp)

# Define a model that outputs the GRU output
model = keras.models.Model(inputs=inp, outputs=gru_out)

x = np.random.normal(size=(2,3,4))
# Get the output of the model and print the result
y = model.predict(x)
print("shape (y) =", y.shape, "\ny = \n", y)
