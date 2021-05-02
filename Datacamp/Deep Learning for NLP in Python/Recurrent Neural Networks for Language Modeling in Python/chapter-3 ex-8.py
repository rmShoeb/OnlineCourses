##################################
# part-1
##################################
# Compute the precision of the sentiment model
prec_sentiment = precision_score(sentiment_y_true, sentiment_y_pred, average=None)
print(prec_sentiment)
##################################
# part-2
##################################
# Compute the recall of the sentiment model
rec_sentiment = recall_score(sentiment_y_true, sentiment_y_pred, average=None)
print(rec_sentiment)
##################################
