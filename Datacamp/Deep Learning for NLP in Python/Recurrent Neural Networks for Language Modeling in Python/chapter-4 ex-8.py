# Instantiate the model
model = Sequential(name="LSTM model")

# Add two LSTM layers
model.add(LSTM(64, input_shape=input_shape, dropout=0.15, recurrent_dropout=0.15, return_sequences=True, name="Input_layer"))
model.add(LSTM(64, dropout=0.15, recurrent_dropout=0.15, return_sequences=False, name="LSTM_hidden"))

# Add the output layer
model.add(Dense(n_vocab, activation='softmax', name="Output_layer"))

# Compile and load weights
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.load_weights('model_weights.h5')
# Summary
model.summary()
