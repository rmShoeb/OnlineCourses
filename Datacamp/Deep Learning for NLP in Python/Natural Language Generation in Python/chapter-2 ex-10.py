# part-1 & 2
# Get the probability distribution of next character
preds = model.predict(X_test, verbose=0)[0]

# Get the index of the most probable next character
next_index = np.argmax(preds)

# Map the index to the actual character and print it
next_char = idx_to_char[next_index]

# Print the next character
print(next_char)

# Input sequence and generate text
sentence = "that, poor contempt, or claim'd thou sle"
generate_text(sentence, 500)
