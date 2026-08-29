# 🏠 Linear Regression - House Price Prediction

A Machine Learning project demonstrating **Linear Regression**, **Train/Test Split**, and **Regression Model Evaluation**.

## 📌 Project Overview

Linear Regression is a supervised Machine Learning algorithm used to predict continuous numerical values.

In this project, the model learns the relationship between:

- **Input (X):** House Size in square feet
- **Target (y):** House Price in lakh rupees

The dataset is divided into training and testing sets to evaluate the model on unseen data.

## 🧠 Algorithm

**Linear Regression**

```text
House Size
    ↓
Linear Regression
    ↓
Predicted House Price
📊 Dataset

A small manually created dataset is used for learning purposes.

House Size (sq ft)	Price (₹ lakh)
        800	            25
        1000           	32
        1200	        38
        1500          	48
        1800          	55
        2000	        62
        2200	        68
        2500            78

🔀 Train/Test Split

The dataset is divided into training and testing data using train_test_split().

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
Parameters
test_size=0.2 → 20% of the data is used for testing.
random_state=42 → Produces a reproducible split.

⚙️ Model Training

The Linear Regression model is created using:

model = LinearRegression()

The model is trained only on the training data:

model.fit(X_train, y_train)

The test data is kept unseen during training.

🔮 Prediction

The model predicts values for the test dataset:

predictions = model.predict(X_test)

A new house price can also be predicted:

new_house = [[1600]]

predicted_price = model.predict(new_house)

This predicts the price of a 1600 sq ft house.

📏 Model Evaluation

The model is evaluated using the test data.

MAE — Mean Absolute Error
mae = mean_absolute_error(y_test, predictions)

Measures the average absolute difference between actual and predicted values.

Lower is generally better.

MSE — Mean Squared Error
mse = mean_squared_error(y_test, predictions)

Measures the average squared error and gives greater weight to larger errors.

Lower is generally better.

RMSE — Root Mean Squared Error
rmse = np.sqrt(mse)

RMSE is the square root of MSE and is expressed in the same unit as the target.

Lower is generally better.

R² — R-squared
r2 = r2_score(y_test, predictions)

Measures how much of the variation in the target is explained by the model.

Higher is generally better.

🧠 Evaluation Summary

MAE   → Average absolute error
MSE   → Average squared error
RMSE  → Square root of MSE
R²    → Variance explained
MAE / MSE / RMSE → Lower is better
R²               → Higher is better

📐 Model Parameters

Coefficient
model.coef_[0]

Represents the slope of the regression line.

Intercept
model.intercept_

Represents the predicted target value when the input feature is zero.

📈 Visualization

The project generates a visualization showing:

Training data
Test data
Linear Regression line

The output image is saved as:

images/linear_regression_train_test.png

🛠 Technologies Used
Python 3
Scikit-learn
NumPy
Matplotlib


📂 Project Structure
linear_regression_house_price/
│
├── linear_regression_house_price.py
├── README.md
├── requirements.txt
├── .gitignore
└── images/
    └── linear_regression_train_test.png


🚀 How to Run
1. Navigate to the project
cd ~/AI_journey/projects/linear_regression_house_price
2. Install dependencies
pip install -r requirements.txt
3. Run the program
python3 linear_regression_house_price.py


📖 Learning Outcomes

Through this project, I learned:

Linear Regression
Train/Test Split
train_test_split()
test_size
random_state
Training data and testing data
Model training using fit()
Prediction using predict()
MAE
MSE
RMSE
R² score
Model evaluation on unseen data
Generalization
Data visualization


🔮 Future Improvements

Use a larger real-world house price dataset.
Add multiple features such as location, bedrooms, bathrooms, and age.
Use a larger training and testing dataset.
Compare multiple regression algorithms.
Apply cross-validation.
Improve model evaluation using real-world data.

👨‍💻 Author

Jasim AG

GitHub:

https://github.com/Jasim-AG/ai-engineer-journey