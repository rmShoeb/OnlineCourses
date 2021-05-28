# Get encoder internal state by passing a sentence as input
inp_seq = eng_input_data[0:1]
states_val = encoder_model_inf.predict(inp_seq)

# Seed the first character and get output from the decoder 
target_seq = np.zeros((1, 1, len(french_vocab)))
target_seq[0, 0, fra_char_to_idx['\t']] = 1  
decoder_out, decoder_h, decoder_c = decoder_model_inf.predict(x=[target_seq] + states_val)

# Find out the next character from the Decoder output
max_val_index = np.argmax(decoder_out[0,-1,:])
sampled_fra_char = fra_idx_to_char[max_val_index]

# Print the first character predicted by the decoder
print(sampled_fra_char)
