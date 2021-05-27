# Get the word IDs from the treasure map
word_ids = np.argmax(treasure_map, axis=-1)
# Get the sequence length from the treasure map
seq_len = treasure_map.shape[1]

for i in range(treasure_map.shape[0]):
	words = []
	for t in range(seq_len):
      	# Get the word ID for the i-th sentence and t-th position
	    wid = word_ids[i, t]
	    if wid != 0:
          	# Append the word corresponding to wid
	        words.append(index2word[wid])
	print("Instruction ", i+1, ": ", ' '.join(words))
