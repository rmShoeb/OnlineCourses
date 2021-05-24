# Define an input layer with batch size 3 and input size 3
inp = Input(batch_shape=(3,3))
# Get the output of the 3 node Dense layer
pred = Dense(3, activation='softmax', kernel_initializer=init, bias_initializer=init)(inp)
model = Model(inputs=inp, outputs=pred)

names = ["Mark", "John", "Kelly"]
prizes = ["Gift voucher", "Car", "Nothing"]
x = np.array([[5, 0, 1], [0, 3, 1], [2, 2, 1]])
# Compute the model prediction for x
y = model.predict(x)
# Get the most probable class for each sample
classes = np.argmax(y, axis=-1)
print("\n".join(["{} has probabilities {} and wins {}".format(n,p,prizes[c]) \
                 for n,p,c in zip(names, y, classes)]))
