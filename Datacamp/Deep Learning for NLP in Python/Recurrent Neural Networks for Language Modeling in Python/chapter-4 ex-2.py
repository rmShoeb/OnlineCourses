# Transform text into sequence of indexes and pad
X = encode_sequences(sentences)

# Print the sequences of indexes
print(X)

# Translate the sentences
translated = translate_many(model, X)

# Create pandas DataFrame with original and translated
df = pd.DataFrame({'Original': sentences, 'Translated': translated})

# Print the DataFrame
print(df)
