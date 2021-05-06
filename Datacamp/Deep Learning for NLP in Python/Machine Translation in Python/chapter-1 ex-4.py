import numpy as np

def words2onehot(word_list, word2index):
  # Convert words to word IDs
  word_ids = [word2index[w] for w in word_list]
  # Convert word IDs to onehot vectors and return the onehot array
  onehot = to_categorical(word_ids, num_classes=3)
  return onehot

words = ["I", "like", "cats"]
# Convert words to onehot vectors using words2onehot
onehot = words2onehot(words, word2index)
# Print the result as (<word>, <onehot>) tuples
print([(w,ohe.tolist()) for w,ohe in zip(words, onehot)])
