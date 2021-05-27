en_st = ['the united states is sometimes chilly during december , but it is sometimes freezing in june .']
print('English: {}'.format(en_st))

# Convert the English sentence to a sequence
en_seq = sents2seqs('source', en_st, onehot=True, reverse=True)

# Predict probabilities of words using en_seq
fr_pred = model.predict(en_seq)

# Get the sequence indices (max argument) of fr_pred
fr_seq = np.argmax(fr_pred, axis=-1)[0]

# Convert the sequence of IDs to a sentence and print
fr_sent = [fr_id2word[i] for i in fr_seq if i != 0]
print("French (Custom): {}".format(' '.join(fr_sent)))
print("French (Google Translate): les etats-unis sont parfois froids en décembre, mais parfois gelés en juin")
