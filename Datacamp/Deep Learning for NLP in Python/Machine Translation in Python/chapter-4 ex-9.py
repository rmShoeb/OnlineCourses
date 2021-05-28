en_sent = ['the united states is sometimes chilly during december , but it is sometimes freezing in june .']
print('English: {}'.format(en_sent))
en_seq = sents2seqs('source', en_sent, onehot=True, reverse=True)
# Predict the initial decoder state with the encoder
de_s_t = encoder.predict(en_seq)
de_seq = word2onehot(fr_tok, 'sos', fr_vocab)
fr_sent = ''
for i in range(fr_len):    
  # Predict from the decoder and recursively assign the new state to de_s_t
  de_prob, de_s_t = decoder.predict([de_seq, de_s_t])
  # Get the word from the probability output using probs2word
  de_w = probs2word(de_prob, fr_tok)
  # Convert the word to a onehot sequence using word2onehot
  de_seq = word2onehot(fr_tok, de_w, fr_vocab)
  if de_w == 'eos': break
  fr_sent += de_w + ' '
print("French (Ours): {}".format(fr_sent))
print("French (Google Translate): les etats-unis sont parfois froids en décembre, mais parfois gelés en juin")
