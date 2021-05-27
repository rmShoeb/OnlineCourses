# Convert the sentence to a word ID sequence
seq = en_tok.texts_to_sequences(['she likes grapefruit , peaches , and lemons .'])
print('Word ID sequence: ', seq)

# Define a tokenizer with vocabulary size 50 and oov_token 'UNK'
en_tok_new = Tokenizer(num_words=50, oov_token='UNK')

# Fit the tokenizer on en_text
en_tok_new.fit_on_texts(en_text)

# Convert the sentence to a word ID sequence
seq_new = en_tok_new.texts_to_sequences(['she likes grapefruit , peaches , and lemons .'])
print('Word ID sequence (with UNK): ', seq_new)
print('The ID 1 represents the word: ', en_tok_new.index_word[1])
