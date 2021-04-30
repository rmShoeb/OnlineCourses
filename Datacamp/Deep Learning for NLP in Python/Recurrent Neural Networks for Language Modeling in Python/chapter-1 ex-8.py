# Import relevant classes/functions
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# Build the dictionary of indexes
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)

# Change texts into sequence of indexes
texts_numeric = tokenizer.texts_to_sequences(texts)
print("Number of words in the sample texts: ({0}, {1})".format(len(texts_numeric[0]), len(texts_numeric[1])))

# Pad the sequences
texts_pad = pad_sequences(texts_numeric, 60)
print("Now the texts have fixed length: 60. Let's see the first one: \n{0}".format(texts_pad[0]))
