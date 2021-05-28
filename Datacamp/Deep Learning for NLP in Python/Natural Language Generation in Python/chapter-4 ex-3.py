# part-1
# Find the length of the longest prefix
max_len_prefix_sent = max([len(prefix) for prefix in prefix_sentences])

# Find the length of the longest suffix
max_len_suffix_sent = max([len(suffix) for suffix in suffix_sentences])

# part-2
# Define a 3-D zero vector for the prefix sentences
input_data_prefix = np.zeros((len(prefix_sentences), max_len_prefix_sent, 
                              len(vocabulary)), dtype='float32')

# Define a 3-D zero vector for the suffix sentences
input_data_suffix = np.zeros((len(suffix_sentences), max_len_suffix_sent, 
                              len(vocabulary)), dtype='float32')

# Define a 3-D zero vector for the target data
target_data = np.zeros((len(suffix_sentences), max_len_suffix_sent,
                        len(vocabulary)), dtype='float32')
