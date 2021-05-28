# Insert the generated character from last time to the target sequence 
target_seq = np.zeros((1, 1, len(vocabulary)))
target_seq[0, 0, max_val_index] = 1

# Initialize the decoder state to the states from last iteration
states_val = [decoder_h, decoder_c]

# Get decoder output
decoder_out, decoder_h, decoder_c = decoder_model_inf.predict(x=[target_seq] + states_val)

# Get most probable next character and print it.
max_val_index = np.argmax(decoder_out[0,-1,:])
sampled_suffix_char = idx_to_char[max_val_index]
print(sampled_suffix_char)
