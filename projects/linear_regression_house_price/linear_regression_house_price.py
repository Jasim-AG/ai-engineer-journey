from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np 
from sklearn.model_selection import train_test_split
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

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
predicted_price = model.predict([[1600]])
print(f"Predicted price for 1600 sq ft: ₹{predicted_price[0]:.2f} lakh")
print(f"Coefficient (Slope): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

mae = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error: {mae:.2f}")

mse = mean_squared_error(y_test , predictions)
print(f"Mean Squared Error: {mse:.2f}")

rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse:.2f}")

r2 = r2_score(y_test    , predictions)
print(f"R-squared: {r2:.2f}")

plt.scatter(X_test, y_test, label="Actual Data")

plt.plot(X_test  , predictions, label="Regression Line")

plt.xlabel("House Size (sq ft)")
plt.ylabel("House Price (₹ lakh)")
plt.title("Linear Regression - House Price Prediction")
plt.legend()

plt.savefig("images/linear_regression_evaluation.png", dpi=300)
