# part-1
# Create an empty set to contain the English vocabulary 
english_vocab = set()

# Iterate over each English sentence
for eng_line in english_sentences:
  
    # Convert the English line to a set
    eng_line_set = set(eng_line)
    
    # Update English vocabulary with new characters from this line.
    english_vocab = english_vocab.union(eng_line_set)

# Sort the vocabulary
english_vocab = sorted(list(english_vocab))

# part-2
# Create an empty set to contain the French vocabulary 
french_vocab = set()

# Iterate over each French sentence
for fra_line in french_sentences:
  
    # Convert the French line to a set
    fra_line_set = set(fra_line)
    
    # Update French vocabulary with new characters from this line.
    french_vocab = french_vocab.union(fra_line_set)

# Sort the vocabulary
french_vocab = sorted(list(french_vocab))
