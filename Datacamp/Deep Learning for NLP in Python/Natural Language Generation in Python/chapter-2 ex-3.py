# Create a dummy input vector
input_vector = np.random.random((1,8))

# Create a tensorflow session to run the network
sess = tf.InteractiveSession()

# Initialize all the variables
sess.run(tf.global_variables_initializer())

# Evaluate the gradients using the training examples
evaluated_gradients = sess.run(gradients,feed_dict={model.input:input_vector})

# Print gradient values from third layer and two nodes of the second layer
print(evaluated_gradients[4])
print(evaluated_gradients[2][4])
