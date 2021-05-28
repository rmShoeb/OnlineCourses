# Load the weights to the encoder GRU from the trained model
en_gru_w = tr_en_gru.get_weights()
# Set the weights of the encoder GRU of the inference model
en_gru.set_weights(en_gru_w)
# Load and set the weights to the decoder GRU
de_gru.set_weights(tr_de_gru.get_weights())
# Load and set the weights to the decoder Dense
de_dense.set_weights(tr_de_dense.get_weights())
