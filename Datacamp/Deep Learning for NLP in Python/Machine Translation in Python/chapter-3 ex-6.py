n_epochs, bsize = 3, 250

for ei in range(n_epochs):
  for i in range(0,data_size,bsize):
    # Get a single batch of encoder inputs
    en_x = sents2seqs('source', en_text[i:(i+bsize)], onehot=True, reverse=True)
    # Get a single batch of decoder outputs
    de_y = sents2seqs('target', fr_text[i:(i+bsize)], onehot=True)

    # Train the model on a single batch of data
    nmt.train_on_batch(en_x, de_y)
    # Obtain the eval metrics for the training data
    res = nmt.evaluate(en_x, de_y, batch_size=bsize, verbose=0)
    print("{} => Train Loss:{}, Train Acc: {}".format(ei+1,res[0], res[1]*100.0))  
