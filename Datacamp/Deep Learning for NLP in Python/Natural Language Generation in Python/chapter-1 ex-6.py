# Fit the model for 5 epochs using a batch size of 128 
model.fit(input_data, target_data, batch_size=128, epochs=5)

# Create a 3-D zero vector and initialize it with the start token
output_seq = np.zeros((1, max_len+1, len(vocabulary)))
output_seq[0, 0, char_to_idx['\t']] = 1

# Get the probabilities for the first character
probs = model.predict_proba(output_seq, verbose=0)[:,1,:]

# Sample vocabulary to get first character
first_char = np.random.choice(sorted(list(vocabulary)), replace=False, p=probs.reshape(len(vocabulary)))

# Print the character generated
print(first_char)
