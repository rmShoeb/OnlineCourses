# Get the numerical ids of column label
numerical_ids = df.label.cat.codes

# Print initial shape
print(numerical_ids.shape)

# One-hot encode the indexes
Y = to_categorical(numerical_ids)

# Check the new shape of the variable
print(Y.shape)

# Print the first 5 rows
print(Y[:5])
