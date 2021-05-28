# Import the layers submodule from keras
import tensorflow.keras.layers as layers

en_inputs = layers.Input(shape=(en_len, en_vocab))
en_gru = layers.GRU(hsize, return_state=True)
# Get the encoder output and state
en_out, en_state = en_gru(en_inputs)

# Define the decoder input layer
de_inputs = layers.Input(shape=(fr_len-1, fr_vocab))
de_gru = layers.GRU(hsize, return_sequences=True)
de_out = de_gru(de_inputs, initial_state=en_state)
# Define a TimeDistributed Dense softmax layer with fr_vocab nodes
de_dense = layers.TimeDistributed(layers.Dense(fr_vocab, activation='softmax'))
de_pred = de_dense(de_out)
