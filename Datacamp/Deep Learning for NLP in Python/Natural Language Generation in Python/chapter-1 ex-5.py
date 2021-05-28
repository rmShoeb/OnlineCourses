# Create a Sequential model
model = Sequential()

# Add SimpleRNN layer of 50 units
model.add(SimpleRNN(50, input_shape=(max_len+1, len(vocabulary)), return_sequences=True))

# Add a TimeDistributed Dense layer of size same as the vocabulary
model.add(TimeDistributed(Dense(len(vocabulary), activation='softmax')))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Print the model summary
model.summary()
