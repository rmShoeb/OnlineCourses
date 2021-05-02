# Import plotting package
import matplotlib.pyplot as plt

# Insert lists of accuracy obtained on the validation set
plt.plot(history_no_emb['acc'], marker='o')
plt.plot(history_emb['acc'], marker='o')

# Add extra descriptions to plot
plt.title('Learning with and without pre-trained embedding vectors')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['no_embeddings', 'with_embeddings'], loc='upper left')

# Display the plot
plt.show()
