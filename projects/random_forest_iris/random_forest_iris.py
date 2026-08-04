from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

iris = load_iris()
x = iris.data
y = iris.target

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)
prediction = model.predict(x_test)
accuracy = accuracy_score(y_test, prediction)

print("=" * 45)
print("Random Forest - Iris Classification")
print("=" * 45)

print("\nPredictions:")
print(prediction)

print(f"\nAccuracy : {accuracy*100:.2f}%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, prediction))

print("\nClassification Report:\n")
print(classification_report(y_test, prediction))