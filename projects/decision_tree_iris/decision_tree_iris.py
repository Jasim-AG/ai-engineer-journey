from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.20, random_state=42)
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
prediction = model.predict(x_test)
accuracy = model.score(x_test, y_test)
print("=" * 40)
print("Decision Tree - Iris Classification")
print("=" * 40)
print("\n prediction :", prediction)
print(f"\nAccuracy : {accuracy*100:.2f}%")

