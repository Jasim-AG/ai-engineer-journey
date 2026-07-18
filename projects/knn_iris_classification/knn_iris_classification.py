from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

iris = load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state =42)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train, y_train)
predictions = model.predict(x_test)
accuracy = model.score(x_test, y_test)
print("=" * 40)
print("KNN - Iris Classification")
print("=" * 40)

print("\nPredictions:")
print(predictions)
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print(f"\nAccuracy: {accuracy * 100:.2f}%")
