from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt

# House size in square feet
X = [
    [800],
    [1000],
    [1200],
    [1500],
    [1800],
    [2000],
    [2200],
    [2500]
]

# House price in lakhs
y = [
    25,
    32,
    38,
    48,
    55,
    62,
    68,
    78
]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict test data
predictions = model.predict(X_test)

# Evaluation metrics
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

print("\n" + "=" * 50)
print("Train/Test Evaluation")
print("=" * 50)

print(f"Mean Absolute Error: {mae:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
print(f"Root Mean Squared Error: {rmse:.2f}")
print(f"R-squared: {r2:.2f}")

# Cross-Validation
cv_scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="r2"
)

print("\n" + "=" * 50)
print("5-Fold Cross-Validation")
print("=" * 50)

for i, score in enumerate(cv_scores, 1):
    print(f"Fold {i}: {score:.2f}")

mean_cv_score = cv_scores.mean()

print(f"\nMean Cross-Validation R²: {mean_cv_score:.2f}")

# Predict a new house
new_house = [[1600]]

predicted_price = model.predict(new_house)

print(
    f"\nPredicted price for 1600 sq ft: "
    f"₹{predicted_price[0]:.2f} lakh"
)

print(f"Coefficient (Slope): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

# Visualization
plt.scatter(X_train, y_train, label="Training Data")
plt.scatter(X_test, y_test, label="Test Data")

X_line = sorted(X)
X_line = [[value[0]] for value in X_line]

plt.plot(
    X_line,
    model.predict(X_line),
    label="Regression Line"
)

plt.xlabel("House Size (sq ft)")
plt.ylabel("House Price (₹ lakh)")
plt.title("Linear Regression - Cross-Validation")
plt.legend()

plt.savefig(
    "images/linear_regression_cross_validation.png",
    dpi=300
)