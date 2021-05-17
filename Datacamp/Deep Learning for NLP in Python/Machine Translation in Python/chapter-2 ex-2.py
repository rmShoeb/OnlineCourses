# Compute length of sentences
sent_lengths = [len(en_sent.split(" ")) for en_sent in en_text]
# Compute the mean of sentences lengths
mean_length = np.mean(sent_lengths)
print('(English) Mean sentence length: ', mean_length)

all_words = []
for sent in en_text:
  # Populate all_words with all the words in sentences
  all_words.extend(sent.split(" "))
# Compute the length of the set containing all_words
vocab_size = len(set(all_words))
print("(English) Vocabulary size: ", vocab_size)
