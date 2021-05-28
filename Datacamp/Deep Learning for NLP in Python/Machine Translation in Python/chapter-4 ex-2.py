# Import the Keras Model object
from tensorflow.keras.models import Model

# Define a model
nmt_tf = Model(inputs=[en_inputs, de_inputs], outputs=de_pred)
# Compile the model with optimizer and loss
nmt_tf.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["acc"])
# Print the summary of the model
nmt_tf.summary()
