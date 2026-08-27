from sklearn.linear_model import LinearRegression
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

model = LinearRegression()
model.fit(X, y)
predicted_price = model.predict([[1600]])
print(f"Predicted price for 1600 sq ft: ₹{predicted_price[0]:.2f} lakh")
print(f"Coefficient (Slope): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

plt.scatter(X, y)

plt.plot(X, model.predict(X))

plt.xlabel("House Size (sq ft)")
plt.ylabel("House Price (₹ lakh)")
plt.title("Linear Regression - House Price Prediction")

plt.savefig("images/linear_regression.png", dpi=300)

