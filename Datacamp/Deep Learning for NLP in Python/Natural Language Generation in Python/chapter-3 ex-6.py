# part-1
# Create input layer
encoder_input = Input(shape=(None, len(english_vocab)))

# Create LSTM Layer of size 256
encoder_LSTM = LSTM(256, return_state = True)

# Save encoder output, hidden and cell state
encoder_outputs, encoder_h, encoder_c = encoder_LSTM(encoder_input)

# Save encoder states
encoder_states = [encoder_h, encoder_c]

# part-2
# Create decoder input layer
decoder_input = Input(shape=(None, len(french_vocab)))

# Create LSTM layer of size 256
decoder_LSTM = LSTM(256, return_sequences=True, return_state = True)

# Save decoder output
decoder_out, _ , _ = decoder_LSTM(decoder_input, initial_state=encoder_states)

# Create a Dense layer with softmax activation
decoder_dense = Dense(len(french_vocab), activation='softmax')

# Save the decoder output
decoder_out = decoder_dense(decoder_out)
