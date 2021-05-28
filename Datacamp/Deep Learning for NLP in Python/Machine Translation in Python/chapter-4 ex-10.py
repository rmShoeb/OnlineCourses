from sklearn.metrics.pairwise import cosine_similarity

# Print the length of the cat_vector
print('Length of the cat_vector: ', cat_vector.size)

# Compute and print the similarity between cat and window vectors
dist_cat_window = cosine_similarity(cat_vector, window_vector)
print('Similarity(cat, window): ', dist_cat_window)

# Compute and print the similarity between cat and dog vectors
print('Similarity(cat,dog): ', cosine_similarity(cat_vector, dog_vector))
