from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import confusion_matrix,classification_report
import matplotlib.pyplot as plt

iris = load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.20, random_state=42)
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
prediction = model.predict(x_test)
cm= confusion_matrix(y_test, prediction)
accuracy = model.score(x_test, y_test)
print("=" * 40)
print("Decision Tree - Iris Classification")
print("=" * 40)
print("\n prediction :", prediction)
print(f"\nAccuracy : {accuracy*100:.2f}%")
print(f"\nConfusion Matrix :\n{cm}")
print("\nClassification Report :")
print("\n", classification_report(y_test, prediction))
plt.figure(figsize=(15, 10))
plot_tree(model, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.tight_layout()
plt.savefig("images/decision_tree.png", dpi=300)
print("Decision tree saved as images/decision_tree.png")
print("\nFeature Importance:\n")
for feature, importance in zip(iris.feature_names, model.feature_importances_):
    print(f"{feature}: {importance:.4f}")