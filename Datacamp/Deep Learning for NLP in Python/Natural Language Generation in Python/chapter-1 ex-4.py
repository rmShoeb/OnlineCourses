# Iterate for each name in the dataset
for n_idx, name in enumerate(names_df['input']):
  # Iterate over each character and convert it to a one-hot encoded vector
  for c_idx, char in enumerate(name):
    input_data[n_idx, c_idx, char_to_idx[char]] = 1

# Iterate for each name in the dataset
for n_idx, name in enumerate(names_df['target']):
  # Iterate over each character and convert it to a one-hot encoded vector
  for c_idx, char in enumerate(name):
    target_data[n_idx, c_idx, char_to_idx[char]] = 1
