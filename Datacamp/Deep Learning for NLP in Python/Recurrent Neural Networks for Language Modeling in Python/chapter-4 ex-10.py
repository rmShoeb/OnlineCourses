# Initialize the variable
Y = transform_text_to_sequences(en_sentences, output_tokenizer)

# Temporary list
ylist = list()
for sequence in Y:
  	# One-hot encode sentence and append to list
    ylist.append(to_categorical(sequence, num_classes=en_vocab_size))

# Update the variable
Y = np.array(ylist).reshape(Y.shape[0], Y.shape[1], en_vocab_size)

# Print the raw sentence and its transformed version
print("Raw sentence: {0}\nTransformed: {1}".format(en_sentences[0], Y[0]))
