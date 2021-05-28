for ei in range(n_epochs):
  for i in range(0,train_size,bsize):    
    en_x = sents2seqs('source', tr_en[i:i+bsize], onehot=True, reverse=True)
    de_xy = sents2seqs('target', tr_fr[i:i+bsize], onehot=True)
    # Create a single batch of decoder inputs and outputs
    de_x, de_y = de_xy[:,:-1,:], de_xy[:,1:,:]
    # Train the model on a single batch of data
    nmt_tf.train_on_batch([en_x,de_x], de_y)
  v_en_x = sents2seqs('source', v_en, onehot=True, reverse=True)
  # Create a single batch of validation decoder inputs and outputs
  v_de_xy = sents2seqs('target', v_fr, onehot=True)
  v_de_x, v_de_y = v_de_xy[:,:-1,:], v_de_xy[:,1:,:]
  # Evaluate the trained model on the validation data
  res = nmt_tf.evaluate([v_en_x,v_de_x], v_de_y, batch_size=valid_size, verbose=0)
  print("{} => Loss:{}, Val Acc: {}".format(ei+1,res[0], res[1]*100.0))
