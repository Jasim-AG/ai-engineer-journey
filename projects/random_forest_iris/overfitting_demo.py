from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Model 1: Complex Random Forest
model1 = RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    random_state=42
)

model1.fit(X_train, y_train)

train_pred1 = model1.predict(X_train)
test_pred1 = model1.predict(X_test)

print("Complex Model")
print("Training Accuracy:", accuracy_score(y_train, train_pred1))
print("Testing Accuracy:", accuracy_score(y_test, test_pred1))


# Model 2: Regularized Random Forest
model2 = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    min_samples_leaf=5,
    random_state=42
)

model2.fit(X_train, y_train)

train_pred2 = model2.predict(X_train)
test_pred2 = model2.predict(X_test)

print("\nRegularized Model")
print("Training Accuracy:", accuracy_score(y_train, train_pred2))
print("Testing Accuracy:", accuracy_score(y_test, test_pred2))