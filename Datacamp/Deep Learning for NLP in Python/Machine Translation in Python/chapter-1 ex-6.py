# Define the onehot2words function that returns words for a set of onehot vectors
def onehot2words(onehot, index2word):
  ids = np.argmax(onehot, axis=1)
  res = [index2word[id] for id in ids]
  return res
# Define the decoder function that returns reversed onehot vectors
def decoder(context_vector):
  word_ids_rev = context_vector[::-1]
  onehot_rev = to_categorical(word_ids_rev, num_classes=3)
  return onehot_rev
# Convert context to reversed onehot vectors using decoder
onehot_rev = decoder(context)
# Get the reversed words using the onehot2words function
reversed_words = onehot2words(onehot_rev, index2word)
print(reversed_words)
