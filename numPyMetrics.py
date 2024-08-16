from sklearn import metrics

# Assuming you have actual and predicted labels
actual = [0, 1, 1, 0, 1]
predicted = [0, 1, 0, 0, 1]

#accuracy = metrics.accuracy_score(actual, predicted)
accuracy2 = metrics.accuracy_score(actual, predicted)
print(f"Accuracy: {accuracy2}")
