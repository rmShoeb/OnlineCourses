# Create decoder input layer
decoder_input = Input(shape=(None, len(vocabulary)))

# Create LSTM layer of size 256
decoder_LSTM = LSTM(256,return_sequences=True, return_state = True)

# Save decoder output
decoder_out, _ , _ = decoder_LSTM(decoder_input, initial_state=encoder_states)

# Create a `Dense` layer with softmax activation
decoder_dense = Dense(len(vocabulary),activation='softmax')

# Save the decoder output
decoder_out = decoder_dense(decoder_out)
