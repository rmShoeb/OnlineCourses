for ei in range(3):
  for i in range(0, train_size, bsize):    
    en_x = sents2seqs('source', tr_en[i:i+bsize], onehot=False, reverse=True)
    # Get a single batch of French sentences with no onehot encoding
    de_xy = sents2seqs('target', tr_fr[i:i+bsize], onehot=False)
    # Get all words except the last word in that batch
    de_x = de_xy[:,:-1]
    de_xy_oh = sents2seqs('target', tr_fr[i:i+bsize], onehot=True)
    # Get all words except the first from de_xy_oh
    de_y = de_xy_oh[:,1:,:]
    # Training the model on a single batch of data
    nmt_emb.train_on_batch([en_x,de_x], de_y)    
    res = nmt_emb.evaluate([en_x, de_x], de_y, batch_size=bsize, verbose=0)
    print("{} => Loss:{}, Train Acc: {}".format(ei+1,res[0], res[1]*100.0))
