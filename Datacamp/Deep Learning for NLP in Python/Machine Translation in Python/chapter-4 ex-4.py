n_epochs, bsize = 3, 250

for ei in range(n_epochs):
  for i in range(0,data_size,bsize):
    en_x = sents2seqs('source', en_text[i:i+bsize], onehot=True, reverse=True)
    de_xy = sents2seqs('target', fr_text[i:i+bsize], onehot=True)
    # Separate the decoder inputs from de_xy
    de_x = de_xy[:,:-1,:]
    # Separate the decoder outputs from de_xy
    de_y = de_xy[:,1:,:]
    # Train the model on a single batch of data    
    nmt_tf.train_on_batch([en_x, de_x], de_y)    
    # Obtain the eval metrics for the training data
    res = nmt_tf.evaluate([en_x,de_x], de_y, batch_size=bsize, verbose=0)
    print("{} => Train Loss:{}, Train Acc: {}".format(ei+1,res[0], res[1]*100.0))  
