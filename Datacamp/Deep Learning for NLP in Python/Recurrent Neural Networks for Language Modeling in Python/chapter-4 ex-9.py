# Get maximum length of the sentences
pt_length = max([len(sentence.split()) for sentence in pt_sentences])

# Transform text to sequence of numerical indexes
X = input_tokenizer.texts_to_sequences(pt_sentences)

# Pad the sequences
X = pad_sequences(X, maxlen=pt_length, padding='post')

# Print first sentence
print(pt_sentences[0])

# Print transformed sentence
print(X[0])
