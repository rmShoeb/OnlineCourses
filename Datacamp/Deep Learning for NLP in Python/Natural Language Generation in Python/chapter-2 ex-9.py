# Input sequence
sentence = "that, poor contempt, or claim'd thou sle"

# Create a 3-D zero vector to contain the encoding of sentence.
X_test = np.zeros((1, maxlen, len(vocabulary)))

# Iterate over each character and convert them to one-hot encoded vector.
for s_idx, char in enumerate(sentence):
    X_test[0, s_idx, char_to_idx[char]] = 1
    
# Get the probability distribution using model predict
preds = model.predict(X_test, verbose=0)

# Get the probability distribution for the first character after the sequence
preds_next_char = preds[0]
