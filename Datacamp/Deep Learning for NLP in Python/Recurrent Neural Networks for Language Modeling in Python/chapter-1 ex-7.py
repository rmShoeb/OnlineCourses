# Instantiate the class
model = Sequential(name="sequential_model")

# One LSTM layer (defining the input shape because it is the 
# initial layer)
model.add(LSTM(128, input_shape=(None, 10), name="LSTM"))

# Add a dense layer with one unit
model.add(Dense(1, activation="sigmoid", name="output"))

# The summary shows the layers and the number of parameters 
# that will be trained
model.summary()
