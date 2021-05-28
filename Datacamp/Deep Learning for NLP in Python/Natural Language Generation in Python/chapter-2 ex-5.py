# Create empty lists for input and target dataset
input_data = []
target_data = []

# Iterate to get all substrings of length maxlen
for i in range(0, len(text) - maxlen):
    # Find the sequence of length maxlen starting at i
    input_data.append(text[i:i+maxlen])
    
    # Find the next char after this sequence 
    target_data.append(text[i+maxlen])

# Print number of sequences in input data
print('No of Sequences:', len(input_data))
