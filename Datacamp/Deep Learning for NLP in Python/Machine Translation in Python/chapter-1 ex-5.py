def encoder(onehot):
  # Get word IDs from onehot vectors and return the IDs
  word_ids = np.argmax(onehot, axis=1)
  return word_ids

# Define "We like dogs" as words
words = ['We', 'like', 'dogs']
# Convert words to onehot vectors using words2onehot
onehot = words2onehot(words, word2index)
# Get the context vector by using the encoder function
context = encoder(onehot)
print(context)
