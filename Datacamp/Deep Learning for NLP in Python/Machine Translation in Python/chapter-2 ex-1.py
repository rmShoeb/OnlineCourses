# Iterate through the first 5 English and French sentences in the dataset
for en_sent, fr_sent in zip(en_text[:5], fr_text[:5]):  
  print("English: ", en_sent)
  print("\tFrench: ", fr_sent)

# Get the first sentence of the English dataset
first_sent = en_text[0]
print("First sentence: ", first_sent)
# Tokenize the first sentence
first_words = first_sent.split(" ")
# Print the tokenized words
print("\tWords: ", first_words)
