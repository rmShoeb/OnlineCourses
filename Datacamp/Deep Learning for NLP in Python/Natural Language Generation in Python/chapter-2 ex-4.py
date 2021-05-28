# Find the vocabulary
vocabulary = sorted(set(text))

# Print the vocabulary size
print('Vocabulary size:', len(vocabulary))

# Dictionary to save the mapping from char to integer
char_to_idx = { char:idx for idx, char in enumerate(vocabulary) }

# Dictionary to save the mapping from integer to char
idx_to_char = { idx:char for idx, char in enumerate(vocabulary) }

# Print char_to_idx and idx_to_char
print(char_to_idx)
print(idx_to_char)
