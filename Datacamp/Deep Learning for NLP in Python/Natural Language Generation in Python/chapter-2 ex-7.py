# Create Sequential model 
model = Sequential()

# Add an LSTM layer of 128 units
model.add(LSTM(128, input_shape=(maxlen, len(vocabulary))))

# Add a Dense output layer
model.add(Dense(len(vocabulary), activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Print model summary
model.summary()
