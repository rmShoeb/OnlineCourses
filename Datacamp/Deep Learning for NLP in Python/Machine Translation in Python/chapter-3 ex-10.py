# Get the word IDs from the treasure map
word_ids = np.argmax(treasure_map, axis=-1)
# Get the batch size from the treasure map
for i in range(treasure_map.shape[0]):
  	# Get all the words of the i-th sentence using list comprehension
	words = [index2word[wid] for wid in word_ids[i] if wid != 0]
	print("Instruction ", i+1, ": ", ' '.join(words))
