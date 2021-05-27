from tensorflow.keras.models import Model
# Define a model with encoder input and decoder output
nmt = Model(inputs=en_inputs, outputs=de_pred)

# Compile the model with an optimizer and a loss
nmt.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

# View the summary of the model 
nmt.summary()
