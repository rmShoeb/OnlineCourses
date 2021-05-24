from tensorflow.keras.layers import RepeatVector

hsize = 48
fr_len = 20
# Define a RepeatVector layer
de_inputs = RepeatVector(fr_len)(en_state)
# Define a GRU model that returns all outputs
decoder_gru = GRU(hsize, return_sequences=True)
# Get the outputs of the decoder
gru_outputs = decoder_gru(de_inputs, initial_state=en_state)
# Define a model with the correct inputs and outputs
enc_dec = Model(inputs=en_inputs, outputs=gru_outputs)
enc_dec.summary()
