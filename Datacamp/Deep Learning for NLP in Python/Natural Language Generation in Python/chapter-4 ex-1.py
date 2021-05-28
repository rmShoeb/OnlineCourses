# Empty lists to store the prefixes and the suffixes
prefix_sentences = []
suffix_sentences = []

# Create one prefix and one suffix at each character of each email
for email in corpus:
    for index in range(len(email)):
        # Find the prefix and suffix
        prefix = email[: index+1]
        suffix = '\t' + email[index+1 :] + '\n'
        
        # Add the prefix and suffix to the list of prefix and suffix sentences
        prefix_sentences.append(prefix)
        suffix_sentences.append(suffix)
