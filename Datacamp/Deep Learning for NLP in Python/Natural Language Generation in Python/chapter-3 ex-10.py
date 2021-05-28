# Fill up target seq with the new char generated 
target_seq = np.zeros((1, 1, len(french_vocab)))
target_seq[0, 0, max_val_index] = 1

# Get decoder final states from last time
states_val = [decoder_h, decoder_c]

# Generate the next character
decoder_out, decoder_h, decoder_c = decoder_model_inf.predict(x=[target_seq]+states_val)

# Map the prediction to char and print it
max_val_index = np.argmax(decoder_out[0,-1,:])
sampled_fra_char = fra_idx_to_char[max_val_index]

print(sampled_fra_char)
