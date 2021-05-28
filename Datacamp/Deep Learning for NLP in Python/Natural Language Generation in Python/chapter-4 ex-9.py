# Pass input prefix to the Encoder inference model and get the states
inp_seq = input_data_prefix[4:5]
states_val = encoder_model_inf.predict(inp_seq)

# Seed the first character and get output from the decoder 
target_seq = np.zeros((1, 1, len(vocabulary)))
target_seq[0, 0, char_to_idx['\t']] = 1  
decoder_out, decoder_h, decoder_c = decoder_model_inf.predict(x=[target_seq] + states_val)

# Find out the next character from the Decoder output
max_val_index = np.argmax(decoder_out[0,-1,:])
sampled_suffix_char = idx_to_char[max_val_index]

# Print the first character
print(sampled_suffix_char)