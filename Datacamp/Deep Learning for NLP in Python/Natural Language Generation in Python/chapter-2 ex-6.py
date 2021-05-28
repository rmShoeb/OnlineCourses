# Create a 3-D zero vector to contain the encoded input sequences
x = np.zeros((len(input_data), maxlen, len(vocabulary)), dtype='float32')

# Create a 2-D zero vector to contain the encoded target characters
y = np.zeros((len(target_data), len(vocabulary)), dtype='float32')

# Iterate over the sequences
for s_idx, sequence in enumerate(input_data):
    # Iterate over all characters in the sequence
    for idx, char in enumerate(sequence):
        # Fill up vector x
        x[s_idx, idx, char_to_idx[char]] = 1    
    # Fill up vector y
    y[s_idx, char_to_idx[target_data[s_idx]]] = 1
