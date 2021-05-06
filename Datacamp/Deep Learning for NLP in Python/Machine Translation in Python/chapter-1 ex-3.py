words_1 = ["I", "like", "cats", "We", "like", "dogs", "He", "hates", "rabbits"]
# Call compute_onehot_length on words_1
length_1 = compute_onehot_length(words_1, word2index)

words_2 = ["I", "like", "cats", "We", "like", "dogs", "We", "like", "cats"]
# Call compute_onehot_length on words_2
length_2 = compute_onehot_length(words_2, word2index)

# Print length_1 and length_2
print("length_1 =>", length_1, " and length_2 => ", length_2)
