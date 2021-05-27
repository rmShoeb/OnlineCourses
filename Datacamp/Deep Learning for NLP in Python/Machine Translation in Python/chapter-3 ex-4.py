from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical

def sents2seqs(input_type, sentences, onehot=False, pad_type='post'):
	# Convert sentences to sequences      
    encoded_text = en_tok.texts_to_sequences(sentences)
    # Pad sentences to en_len
    preproc_text = pad_sequences(encoded_text, padding=pad_type, truncating='post', maxlen=en_len)
    if onehot:
		# Convert the word IDs to onehot vectors
        preproc_text = to_categorical(preproc_text, num_classes=en_vocab)
    return preproc_text
sentence = 'she likes grapefruit , peaches , and lemons .'  
# Convert a sentence to sequence by pre-padding the sentence
pad_seq = sents2seqs('source', [sentence], pad_type='pre')
