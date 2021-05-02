def generate_phrase(model, initial_text):
    # Initialize variables  
    res, seq, counter, next_char = initialize_params(initial_text)
    
    # Loop until stop conditions are met
    while counter < 100 and next_char != r'.':
        # but the instructions clearly says 'or'!
      	# Get next char using the model and append to the sentence
        next_char, res, seq = get_next_token(model, res, seq)
        # Update the counter
        counter = counter + 1
    return res
  
# Create a phrase
print(generate_phrase(model, "I am not insane, "))
