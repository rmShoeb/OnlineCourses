# Find the length of the longest English sentence
max_len_eng_sent = max([len(sentence) for sentence in english_sentences])

# Find the length of the longest French sentence
max_len_fra_sent = max([len(sentence) for sentence in french_sentences])

# Create a 3-D zero vector for the input English data
eng_input_data = np.zeros((len(english_sentences), max_len_eng_sent, len(english_vocab)), dtype='float32')

# Create a 3-D zero vector for the input French data
fra_input_data = np.zeros((len(french_sentences), max_len_fra_sent, len(french_vocab)), dtype='float32')

# Create the target vector
target_data = np.zeros((len(french_sentences), max_len_fra_sent, len(french_vocab)), dtype='float32')
