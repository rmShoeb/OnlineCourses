# Define an input layer which accepts a sequence of word IDs
en_inputs = Input(shape=(en_len,))
# Define an Embedding layer which accepts en_inputs
en_emb = Embedding(en_vocab, 96, input_length=en_len)(en_inputs)
en_out, en_state = GRU(hsize, return_state=True)(en_emb)

de_inputs = Input(shape=(fr_len-1,))
# Define an Embedding layer which accepts de_inputs
de_emb = Embedding(fr_vocab, 96, input_length=fr_len-1)(de_inputs)
de_out, _ = GRU(hsize, return_sequences=True, return_state=True)(de_emb, initial_state=en_state)
de_pred = TimeDistributed(Dense(fr_vocab, activation='softmax'))(de_out)

# Define the Model which accepts encoder/decoder inputs and outputs predictions 
nmt_emb = Model([en_inputs, de_inputs], de_pred)
nmt_emb.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
