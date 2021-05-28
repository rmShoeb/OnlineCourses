# Iterate over the 50 sentences
for i in range(50):
    # Iterate over each English character of each sentence
    for k, ch in enumerate(english_sentences[i]):
        # Convert the character to one-hot encoded vector
        eng_input_data[i, k, eng_char_to_idx[ch]] = 1.
    
    # Iterate over each French character of each sentence
    for k, ch in enumerate(french_sentences[i]):
        # Convert the character to one-hot encoded vector
        fra_input_data[i, k, fra_char_to_idx[ch]] = 1.

        # Target data will be one timestep ahead and excludes start character
        if k > 0:
            target_data[i, k-1, fra_char_to_idx[ch]] = 1.
