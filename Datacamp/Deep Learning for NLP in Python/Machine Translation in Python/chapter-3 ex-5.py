sentences = ["california is never rainy during july ."]
# Add new keyword parameter reverse which defaults to False
def sents2seqs(input_type, sentences, onehot=False, pad_type='post', reverse=False):     
    encoded_text = en_tok.texts_to_sequences(sentences)
    preproc_text = pad_sequences(encoded_text, padding=pad_type, truncating='post', maxlen=en_len)
    if reverse:
      # Reverse the text using numpy axis reversing
      preproc_text = preproc_text[:, ::-1]
    if onehot:
        preproc_text = to_categorical(preproc_text, num_classes=en_vocab)
    return preproc_text
# Call sents2seqs to get the padded and reversed sequence of IDs
pad_seq = sents2seqs('source', sentences, reverse=True)
rev_sent = [en_tok.index_word[wid] for wid in pad_seq[0][-6:]] 
print('\tReversed: ',' '.join(rev_sent))
