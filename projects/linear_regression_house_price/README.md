# 🏠 Linear Regression - House Price Prediction & Model Evaluation

A Machine Learning project demonstrating **Linear Regression**, **Train/Test Split**, **Regression Model Evaluation**, and **K-Fold Cross-Validation**.

## 📌 Project Overview

Linear Regression is a supervised Machine Learning algorithm used to predict continuous numerical values.

In this project, the model learns the relationship between:

- **Input (X):** House Size in square feet
- **Target (y):** House Price in lakh rupees

The project uses Train/Test Split for evaluation and K-Fold Cross-Validation for a more robust estimate of model performance.

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
        1000	        32
        1200	        38
        1500	        48
        1800	        55
        2000	        62
        2200	        68
        2500	        78


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

The model is trained using:

model.fit(X_train, y_train)

The test data remains unseen during training.

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

🔁 K-Fold Cross-Validation

K-Fold Cross-Validation evaluates the model multiple times using different portions of the dataset as the test/validation fold.

In this project, 5-fold cross-validation is used:

cv_scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="r2"
)
How K-Fold works
Fold 1 → Test
Fold 2 → Train
Fold 3 → Train
Fold 4 → Train
Fold 5 → Train

Fold 1 → Train
Fold 2 → Test
Fold 3 → Train
Fold 4 → Train
Fold 5 → Train

...

Each fold gets a chance to be used as the test/validation set.

Cross-Validation Scores

The individual fold scores are displayed using:

for i, score in enumerate(cv_scores, 1):
    print(f"Fold {i}: {score:.2f}")
Mean Cross-Validation Score
mean_cv_score = cv_scores.mean()

This calculates the average R² score across all folds.

🧠 Why Cross-Validation?

A single Train/Test Split can depend heavily on which samples happen to be placed in the test set.

K-Fold Cross-Validation evaluates the model on different portions of the dataset and averages the results.

Train/Test Split
→ One split
→ One evaluation

K-Fold Cross-Validation
→ Multiple folds
→ Multiple evaluations
→ Average score

This provides a more robust estimate of model performance.

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

The visualization is saved as:

images/linear_regression_cross_validation.png

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
    └── linear_regression_cross_validation.png


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
K-Fold Cross-Validation
cross_val_score()
cv
scoring
Cross-validation scores
Mean cross-validation score
Model evaluation on unseen data
Generalization
Data visualization


🔮 Future Improvements

Use a larger real-world house price dataset.
Add multiple features such as location, bedrooms, bathrooms, and age.
Use a larger training and testing dataset.
Compare multiple regression algorithms.
Apply cross-validation with different numbers of folds.
Compare different evaluation metrics.
Improve model evaluation using real-world data.

👨‍💻 Author

Jasim AG

GitHub:

https://github.com/Jasim-AG/ai-engineer-journey