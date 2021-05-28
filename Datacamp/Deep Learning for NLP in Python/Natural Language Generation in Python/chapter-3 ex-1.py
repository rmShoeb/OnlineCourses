# Consider only the first 50 lines of the dataset
for i in range(50):
	# Split each line into two at the tab character
    eng_fra_line = str(lines[i]).split('\t')
    
    # Separate out the English sentence 
    eng_line = eng_fra_line[0]
    
    # Append the start and end token to each French sentence
    fra_line = '\t' + eng_fra_line[1] + '\n'
    
    # Append the English and French sentence to the list of sentences
    english_sentences.append(eng_line)
    french_sentences.append(fra_line)
