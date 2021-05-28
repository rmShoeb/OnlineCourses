# Build model
model = Model(inputs=[encoder_input, decoder_input],outputs=[decoder_out])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy')

# Print model summary
model.summary()

# Fit the model
model.fit(x=[input_data_prefix, input_data_suffix], y=target_data,
          batch_size=64, epochs=1, validation_split=0.2)
