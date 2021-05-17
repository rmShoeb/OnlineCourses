import tensorflow.keras as keras

en_len = 15
en_vocab = 150
hsize = 48

# Define an input layer
en_inputs = keras.layers.Input(shape=(en_len, en_vocab))
# Define a GRU layer which returns the state
en_gru = keras.layers.GRU(hsize, return_state=True)
# Get the output and state from the GRU
en_state, en_out = en_gru(en_inputs)
# Define and print the model summary
encoder = keras.models.Model(inputs=en_inputs, outputs=en_out)
print(encoder.summary())
