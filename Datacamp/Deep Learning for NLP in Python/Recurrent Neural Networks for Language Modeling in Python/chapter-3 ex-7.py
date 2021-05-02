# Get probabilities for each class
pred_probabilities = model.predict_proba(X_test)

# Thresholds at 0.5 and 0.8
y_pred_50 = [np.argmax(x) if np.max(x) >= 0.5 else DEFAULT_CLASS for x in pred_probabilities]
y_pred_80 = [np.argmax(x) if np.max(x) >= 0.8 else DEFAULT_CLASS for x in pred_probabilities]

trade_off = pd.DataFrame({
    'Precision_50': precision_score(y_true, y_pred_50, average=None), 
    'Precision_80': precision_score(y_true, y_pred_80, average=None), 
    'Recall_50': recall_score(y_true, y_pred_50, average=None), 
    'Recall_80': recall_score(y_true, y_pred_80, average=None)}, 
  index=['Class 1', 'Class 2', 'Class 3'])

print(trade_off)
