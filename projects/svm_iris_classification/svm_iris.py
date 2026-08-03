from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

iris = load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=42)
model = SVC(kernel="linear")
model.fit(x_train, y_train)
pred = model.predict(x_test)
accuracy = accuracy_score(y_test,pred)
print("=" * 40)
print("Support Vector Machine - Iris Classification")
print("=" * 40)

print("\nPredictions:")
print(pred)

print(f"\nAccuracy : {accuracy * 100:.2f}%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, pred))

print("\nClassification Report:\n")
print(classification_report(y_test, pred))