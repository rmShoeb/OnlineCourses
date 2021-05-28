# Create a sequential model
model = Sequential()

# Create a dense layer of 12 units
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))

# Create a dense layer of 8 units
model.add(Dense(8, init='uniform', activation='relu'))

# Create a dense layer of 1 unit
model.add(Dense(1, init='uniform', activation='sigmoid'))

# Compile the model and get gradients
model.compile(loss='binary_crossentropy', optimizer='adam')
gradients = backend.gradients(model.output, model.trainable_weights)
