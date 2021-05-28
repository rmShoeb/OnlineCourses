# Create the input layer of the encoder
encoder_input = Input(shape=(None, len(vocabulary)))

# Create LSTM Layer of size 256
encoder_LSTM = LSTM(256, return_state = True)

# Save encoder output, hidden and cell state
encoder_outputs, encoder_h, encoder_c = encoder_LSTM(encoder_input)

# Save encoder states
encoder_states = [encoder_h, encoder_c]
