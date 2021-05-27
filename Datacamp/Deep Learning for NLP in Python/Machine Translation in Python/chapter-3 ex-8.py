# Convert validation data to onehot
v_en_x = sents2seqs('source', v_en, onehot=True, reverse=True)
v_de_y = sents2seqs('target', v_fr, onehot=True)

n_epochs, bsize = 3, 250
for ei in range(n_epochs):
  for i in range(0,train_size,bsize):
    # Get a single batch of inputs and outputs
    en_x = sents2seqs('source', tr_en[i:i+bsize], onehot=True, reverse=True)
    de_y = sents2seqs('target', tr_fr[i:i+bsize], onehot=True)
    # Train the model on a single batch of data
    nmt.train_on_batch(en_x, de_y)
  # Evaluate the trained model on the validation data
  res = nmt.evaluate(v_en_x, v_de_y, batch_size=valid_size, verbose=0)
  print("{} => Loss:{}, Val Acc: {}".format(ei+1,res[0], res[1]*100.0))
