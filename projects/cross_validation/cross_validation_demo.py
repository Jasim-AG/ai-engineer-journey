
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create K-Fold
kfold = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

# Create model
model = DecisionTreeClassifier(random_state=42)

# Perform cross-validation
scores = cross_val_score(
    model,
    X,
    y,
    cv=kfold,
    scoring="accuracy"
)

# Display results
print("Individual Fold Scores:", scores)
print("Average Accuracy:", np.mean(scores))
print("Standard Deviation:", np.std(scores))
