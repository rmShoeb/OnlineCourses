# Function to predict many phrases
def predict_many(model, sentences, index_to_word, raw_dataset):
    for i, sentence in enumerate(sentences):
        # Translate the Portuguese sentence
        translation = predict_one(model, sentence, index_to_word)
        
        # Get the raw Portuguese and English sentences
        raw_target, raw_src = raw_dataset[i]
        
        # Print the correct Portuguese and English sentences and the predicted
        print('src=[%s], target=[%s], predicted=[%s]' % (raw_src, raw_target, translation))

predict_many(model, X_test[:10], en_index_to_word, test)
