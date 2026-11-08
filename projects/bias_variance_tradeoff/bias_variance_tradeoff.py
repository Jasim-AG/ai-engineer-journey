import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

# Generate dataset
np.random.seed(42)

X = np.linspace(-3, 3, 30).reshape(-1, 1)
y = X.ravel() ** 2 + np.random.randn(30) * 2

X_plot = np.linspace(-3, 3, 200).reshape(-1, 1)

# Different model complexities
degrees = [1, 2, 15]

plt.figure(figsize=(12, 5))

for degree in degrees:

    model = make_pipeline(
        PolynomialFeatures(degree),
        LinearRegression()
    )

    model.fit(X, y)

    predictions = model.predict(X_plot)
    train_predictions = model.predict(X)

    error = mean_squared_error(y, train_predictions)

    print(f"Degree: {degree}")
    print(f"Training Error: {error:.2f}")
    print("-" * 30)

    plt.plot(
        X_plot,
        predictions,
        label=f"Degree {degree}"
    )

plt.scatter(X, y, color="black", label="Actual Data")

plt.title("Bias-Variance Tradeoff")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()

plt.show()