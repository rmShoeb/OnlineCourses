# Create and fit tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(news_dataset.data)

# Prepare the data
prep_data = tokenizer.texts_to_sequences(news_dataset.data)
prep_data = pad_sequences(prep_data, maxlen=200)

# Prepare the labels
prep_labels = to_categorical(news_dataset.target)

# Print the shapes
print(prep_data.shape)
print(prep_labels.shape)
