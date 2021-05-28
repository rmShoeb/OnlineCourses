# part-1
# Generate 10 French sentences from inp_seq
for seq_index in range(10):
  
    # Get next encoded english sentence
    inp_seq = eng_input_data[seq_index:seq_index+1]
    
    # Get the translated sentence
    translated_sent = translate_eng_sentence(inp_seq)
    
    # Print the original English sentence
    print('English sentence:', english_sentences[seq_index])
    
    # Print the translated French sentence
    print('French sentence:', translated_sent)
