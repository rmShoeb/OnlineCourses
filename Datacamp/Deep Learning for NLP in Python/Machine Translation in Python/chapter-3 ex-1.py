from tensorflow.keras.preprocessing.text import Tokenizer

# Define a Keras Tokenizer
en_tok = Tokenizer()

# Fit the tokenizer on some text
en_tok.fit_on_texts(en_text)

for w in ["january", "apples", "summer"]:
  # Get the word ID of word w
  id = en_tok.word_index[w]
  # Print the word and the word ID
  print(w, " has id: ", id)
