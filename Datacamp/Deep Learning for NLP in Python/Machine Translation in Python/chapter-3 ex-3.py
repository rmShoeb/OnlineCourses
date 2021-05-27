fr_text_new = []

# Loop through all sentences in fr_text
for sent in fr_text:
  
  print("Before adding tokens: ", sent)
  
  # Add sos and eos tokens using string.join
  sent_new = " ".join(['sos', sent, 'eos'])
  # Append the modified sentence to fr_text_new
  fr_text_new.append(sent_new)
  
  # Print sentence after adding tokens
  print("After adding tokens: ", sent_new, '\n')
