# Create lists to keep the sentences and the next character
sentences = []   # ~ Training data
next_chars = []  # ~ Training labels

# Define hyperparameters
step = 2          # ~ Step to take when reading the texts in characters
chars_window = 10 # ~ Number of characters to use to predict the next one  

# Loop over the text: length `chars_window` per time with step equal to `step`
for i in range(0, len(sheldon_quotes) - chars_window, step):
    sentences.append(sheldon_quotes[i:i + chars_window])
    next_chars.append(sheldon_quotes[i+chars_window])

# Print 10 pairs
print_examples(sentences, next_chars, 10)
