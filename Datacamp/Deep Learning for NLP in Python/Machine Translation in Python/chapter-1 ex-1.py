from tensorflow.python.keras.utils import to_categorical

# Create a list of words and convert them to indices
words = ["I", "like", "cats"]
word_ids = [word2index[w] for w in words]
print(word_ids)

# Create onehot vectors using to_categorical function
onehot_1 = to_categorical(word_ids)
# Print words and their corresponding onehot vectors
print([(w,ohe.tolist()) for w,ohe in zip(words, onehot_1)])

# Create onehot vectors with a fixed number of classes and print the result
onehot_2 = to_categorical(word_ids, num_classes=5)

print([(w,ohe.tolist()) for w,ohe in zip(words, onehot_2)])
