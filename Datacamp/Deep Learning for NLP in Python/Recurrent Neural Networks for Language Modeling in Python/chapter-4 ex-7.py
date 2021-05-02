# Instantiate the variables with zeros
numerical_sentences = np.zeros((len(sentences), chars_window, n_vocab), dtype=np.bool)
numerical_next_chars = np.zeros((num_seqs, n_vocab), dtype=np.bool)

# Loop for every sentence
for i, sentence in enumerate(sentences):
  # Loop for every character in sentence
  for t, char in enumerate(sentence):
    # Set position of the character to 1
    numerical_sentences[i, t, char_to_index[char]] = 1
    # Set next character to 1
    numerical_next_chars[i, char_to_index[next_chars[i]]] = 1

# Print the first position of each
print(numerical_sentences[0], numerical_next_chars[0], sep="\n")
