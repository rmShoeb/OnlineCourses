# Build model
model = Model(inputs=[encoder_input, decoder_input],outputs=[decoder_out])

# Compile the model
model.compile(optimizer='rmsprop', loss='categorical_crossentropy')

# Print model summary
model.summary()

# Fit the model
model.fit(x=[eng_input_data, fra_input_data], y=target_data,
          		batch_size=64, epochs=1, validation_split=0.2)
