for i in range(len(prefix_sentences)):
    # Iterate over each character in each prefix
    for k, ch in enumerate(prefix_sentences[i]):
        # Convert the character to a one-hot encoded vector
        input_data_prefix[i, k, char_to_idx[ch]] = 1
        
    # Iterate over each character in each suffix
    for k, ch in enumerate(suffix_sentences[i]):
        # Convert the character to a one-hot encoded vector
        input_data_suffix[i, k, char_to_idx[ch]] = 1

        # Target data is one timestep ahead and excludes start character
        if k > 0:
            target_data[i, k-1, char_to_idx[ch]] = 1
