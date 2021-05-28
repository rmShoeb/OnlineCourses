# Insert a tab in front of all the names
names_df['input'] = names_df['input'].apply(lambda x : '\t' + x)

# Append a newline at the end of every name
# We already appended a tab in front, so the target word should start at index 1
names_df['target'] = names_df['input'].apply(lambda x : x[1:len(x)] + '\n')
