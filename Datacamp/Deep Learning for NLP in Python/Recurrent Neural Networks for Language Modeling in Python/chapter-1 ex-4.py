# Transform the list of sentences into a list of words
all_words = ' '.join(sheldon_quotes).split(' ')

# Get number of unique words
unique_words = list(set(all_words))

# Dictionary of indexes as keys and words as values
index_to_word = {i:wd for i, wd in enumerate(sorted(unique_words))}

print(index_to_word)

# Dictionary of words as keys and indexes as values
word_to_index = {wd:i for (i,wd) in enumerate(sorted(unique_words))}

print(word_to_index)
