# part-1
# Generate 10 suffixes
for seq_index in range(10):
  
    # Get the next tokenized sentence
    inp_seq = input_data_prefix[seq_index:seq_index+1]
    
    # Generate the suffix sentence
    suffix_sent = generate_suffix_sentence(inp_seq)
    
    # Print the prefix sentence
    print('Prefix Sentence:', prefix_sentences[seq_index])
    
    # Print the suffix sentence
    print('Suffix Sentence:', suffix_sent)
