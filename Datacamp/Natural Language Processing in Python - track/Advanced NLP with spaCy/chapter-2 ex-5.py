# part-2
# # Get all tokens and part-of-speech tags
# pos_tags = [token.pos_ for token in doc]

# for index, pos in enumerate(pos_tags):
#     # Check if the current token is a proper noun
#     if pos == 'PROPN':
#         # Check if the next token is a verb
#         if pos_tags[index + 1] == 'VERB':
#             print('Found a verb after a proper noun!')
for token in doc:
    if token.pos_ == 'PROPN':
        if doc[token.i+1].pos_ == 'VERB':
            print('Found a verb after a proper noun!')
