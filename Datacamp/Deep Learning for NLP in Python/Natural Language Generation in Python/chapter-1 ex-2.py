# Get the vocabulary
vocabulary = get_vocabulary(names_df['input'])

# Sort the vocabulary
vocabulary_sorted = sorted(vocabulary)

# Create the mapping of the vocabulary chars to integers
char_to_idx = { char : idx for idx, char in enumerate(vocabulary_sorted) }

# Create the mapping of the integers to vocabulary chars
idx_to_char = { idx:char for idx, char in enumerate(vocabulary_sorted) }

# Print the dictionaries
print(char_to_idx)
print(idx_to_char)
