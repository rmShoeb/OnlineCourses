# Print names and x
print('names=\n',names, '\nx=\n',x, '\nx.shape=', x.shape)

inp = Input(shape=(2, 3))
# Create the TimeDistributed layer (the output of the Dense layer)
dense_time = TimeDistributed(Dense(3, activation='softmax', kernel_initializer=init, bias_initializer=init))
pred = dense_time(inp)
model = Model(inputs=inp, outputs=pred)

y = model.predict(x)
# Get the most probable class for each sample
classes = np.argmax(y, axis=-1)
for t in range(2):
  # Get the t-th time-dimension slice of y and classes
  for n, p, c in zip(names[t], y[:, t, :], classes[:, t]):
  	print("Game {}: {} has probs {} and wins {}\n".format(t+1,n,p,prizes[c]))
