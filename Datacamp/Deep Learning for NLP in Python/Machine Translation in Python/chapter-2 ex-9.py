# Import Dense and TimeDistributed layers
from tensorflow.keras.layers import Dense, TimeDistributed
# Define a softmax dense layer that has fr_vocab outputs
de_dense = Dense(fr_vocab, activation='softmax')
# Wrap the dense layer in a TimeDistributed layer
de_dense_time = TimeDistributed(de_dense)
# Get the final prediction of the model
de_pred = de_dense_time(de_out)
print("Prediction shape: ", de_pred.shape)
