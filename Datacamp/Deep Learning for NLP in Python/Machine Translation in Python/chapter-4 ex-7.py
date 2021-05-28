import tensorflow.keras.layers as layers
from tensorflow.keras.models import Model
# Define an input layer that accepts a single onehot encoded word
de_inputs = layers.Input(shape=(1, fr_vocab))
# Define an input to accept the t-1 state
de_state_in = layers.Input(shape=(hsize,))
de_gru = layers.GRU(hsize, return_state=True)
# Get the output and state from the GRU layer
de_out, de_state_out = de_gru(de_inputs, initial_state=de_state_in)
de_dense = layers.Dense(fr_vocab, activation='softmax')
de_pred = de_dense(de_out)

# Define a model
decoder = Model(inputs=[de_inputs, de_state_in], outputs=[de_pred, de_state_out])
print(decoder.summary())
