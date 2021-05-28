# Initialize vocabulary with the start and end token
vocabulary = set(['\t', '\n'])

# Iterate for each char in each email
for email in corpus:
    for char in email:
        # Add the char if not in vocabulary, 
        if (char not in vocabulary):
            vocabulary.add(char)            
# Sort the vocabulary
vocabulary = sorted(vocabulary)

# Create char to int and int to char mapping
char_to_idx = dict((char, idx) for idx, char in enumerate(vocabulary))
idx_to_char = dict((idx, char) for idx, char in enumerate(vocabulary))
