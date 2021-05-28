bsize = 250
for i in range(0, len(en_text), bsize):
  # Get the encoder inputs using the sents2seqs() function
  en_x = sents2seqs('source', en_text[i:i+bsize], onehot=True, reverse=True)
  # Get the decoder inputs/outputs using the sents2seqs() function
  de_xy = sents2seqs('target', fr_text[i:i+bsize], onehot=True)
  # Separate the decoder inputs from de_xy
  de_x = de_xy[:,:-1,:]
  # Separate the decoder outputs from de_xy
  de_y = de_xy[:,1:,:]
  
  print("Data from ", i, " to ", i+bsize)
  print("\tnp.argmax() => en_x[0]: ", np.argmax(en_x[0], axis=-1))
  print("\tnp.argmax() => de_x[0]: ", np.argmax(de_x[0], axis=-1))
  print("\tnp.argmax() => de_y[0]: ", np.argmax(de_y[0], axis=-1))
