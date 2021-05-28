# Find the length of longest name
max_len = get_max_len(names_df['input'])

# Initialize the input vector
input_data = np.zeros((len(names_df['input']), max_len+1, len(vocabulary)), dtype='float32')

# Initialize the target vector
target_data = np.zeros((len(names_df['target']), max_len+1, len(vocabulary)), dtype='float32')
