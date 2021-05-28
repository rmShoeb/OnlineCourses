# part-1
# Print the first character which we got last time
print(first_char)

# Update the vector to contain first the character
output_seq[0, 1, char_to_idx[first_char]] = 1

# Get the probabilities for the second character
probs = model.predict_proba(output_seq, verbose=0)[:,2,:]

# Sample vocabulary to get second character
second_char = np.random.choice(sorted(list(vocabulary)), replace=False, p=probs.reshape(len(vocabulary)))

# Print the second character
print(second_char)
