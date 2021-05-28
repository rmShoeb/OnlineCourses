# Create encoder inference model
encoder_model_inf = Model(encoder_input, encoder_states)

# Create decoder input states for inference
decoder_state_input_h = Input(shape=(256,))
decoder_state_input_c = Input(shape=(256,))
decoder_input_states = [decoder_state_input_h, decoder_state_input_c]

# Create decoder output states for inference
decoder_out, decoder_h, decoder_c = decoder_LSTM(decoder_input, initial_state=decoder_input_states)
decoder_states = [decoder_h , decoder_c]

# Create decoder dense layer
decoder_out = decoder_dense(decoder_out)
decoder_model_inf = Model(inputs=[decoder_input] + decoder_input_states, outputs=[decoder_out] + decoder_states )