from tensorflow.keras.layers import Input, RepeatVector
from tensorflow.keras.models import Model
import numpy as np

inp = Input(shape=(2,))
# Define a RepeatVector that repeats the input 6 times
rep = RepeatVector(6)(inp)
# Define a model
model = Model(inputs=inp, outputs=rep)
# Define input x
x = np.array([[0,1], [2,3]])
# Get model prediction y
y = model.predict(x)
print('x.shape = ',x.shape,'\ny.shape = ',y.shape)
