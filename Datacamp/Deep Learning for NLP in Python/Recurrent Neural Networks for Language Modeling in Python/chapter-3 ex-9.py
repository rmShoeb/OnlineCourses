# Use the model to predict on new data
predicted = model.predict(X_test)

# Choose the class with higher probability 
y_pred = np.argmax(predicted, axis=1)

# Compute and print the confusion matrix
print(confusion_matrix(y_true, y_pred))

# Create the performance report
print(classification_report(y_true, y_pred, target_names=news_cat))
