# Word2Vec model
w2v_model = Word2Vec.load('bigbang_word2vec.model')

# Selected words to check similarities
words_of_interest = ["bazinga", "penny", "universe", "spock", "brain"]

# Compute top 5 similar words for each of the words of interest
top5_similar_words = []
for word in words_of_interest:
    top5_similar_words.append(
      {word: [item[0] for item in w2v_model.wv.most_similar([word], topn=5)]}
    )

# Print the similar words
print(top5_similar_words)
