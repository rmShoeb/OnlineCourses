# Define the Input layer
inp = keras.layers.Input(batch_shape=(3,20,5))
# Define a GRU layer that takes in inp as the input
gru_out1 = keras.layers.GRU(10)(inp)
print("gru_out1.shape = ", gru_out1.shape)

# Define the second GRU and print the shape of the outputs
gru_out2, gru_state = keras.layers.GRU(10, return_state=True)(inp)
print("gru_out2.shape = ", gru_out2.shape)
print("gru_state.shape = ", gru_state.shape)

# Define the third GRU layer which will return all the outputs
gru_out3 = keras.layers.GRU(10, return_sequences=True)(inp)
print("gru_out3.shape = ", gru_out3.shape)
