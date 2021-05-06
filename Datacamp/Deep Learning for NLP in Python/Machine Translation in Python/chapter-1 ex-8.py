# Define an input layer
inp = keras.layers.Input(shape=(3,4))
# Define a GRU layer that takes in the input
gru_out = keras.layers.GRU(10)(inp)
# Define a model that outputs the GRU output
model = keras.models.Model(inputs=inp, outputs=gru_out)

x1 = np.random.normal(size=(2,3,4))
x2 = np.random.normal(size=(5,3,4))

# Get the output of the model and print the result
y1 = model.predict(x1)
y2 = model.predict(x2)
print("shape (y1) = ", y1.shape, " shape (y2) = ", y2.shape)
