def compute_onehot_length(words, word2index):
  # Create word IDs for words
  word_ids = [word2index[w] for w in words]
  # Convert word IDs to onehot vectors
  onehot = to_categorical(word_ids)
  # Return the length of a single one-hot vector
  return onehot.shape[1]

word2index = {"He":0, "drank": 1, "milk": 2}
# Compute and print onehot length of a list of words
print(compute_onehot_length(['He','drank','milk'], word2index))
