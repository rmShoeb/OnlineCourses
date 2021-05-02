# See example article
print(news_dataset.data[5])

# Transform the text into numerical indexes
news_num_indices = tokenizer.texts_to_sequences(news_dataset.data)

# Print the transformed example article
print(news_num_indices[5])

# Transform the labels into one-hot encoded vectors
labels_onehot = to_categorical(news_dataset.target)

# Check before and after for the sample article
print("Before: {0}\nAfter: {1}".format(news_dataset.target[5], labels_onehot[5]))
