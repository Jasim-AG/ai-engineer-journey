# 🏠 Linear Regression - House Price Prediction

A Machine Learning project that uses **Linear Regression** to predict house prices based on house size.

## 📌 Project Overview

Linear Regression is a supervised Machine Learning algorithm used to predict continuous numerical values.

In this project, the model learns the relationship between:

- **Input (X):** House Size in square feet
- **Target (y):** House Price in lakh rupees

After training, the model predicts the price of a new house based on its size.

## 🧠 Algorithm

**Linear Regression**

The model learns a best-fit straight line between house size and house price.

```text
House Size
    ↓
Linear Regression
    ↓
House Price


📊 Dataset

This project uses a small manually created dataset for learning purposes.

House Size (sq ft)	Price (₹ lakh)
        800	             25
        1000	         32
        1200	         38
        1500	         48
        1800	         55
        2000	         62
        2200	         68
        2500	         78


⚙️ Model Training

The model is created using:

model = LinearRegression()

It is trained using:

model.fit(X, y)

The model learns the relationship between house size and house price.

🔮 Prediction

The project predicts the price of a 1600 sq ft house:

prediction = model.predict([[1600]])

The trained model uses the learned slope and intercept to make the prediction.

📐 Model Parameters
Coefficient
model.coef_[0]

The coefficient represents the slope of the regression line.

It indicates how much the predicted house price changes when house size increases by one square foot.

Intercept
model.intercept_

The intercept represents the predicted target value when the input feature is zero.

📈 Visualization

The project generates a scatter plot showing the original house-price data and the Linear Regression line.

The output image is saved at:

images/linear_regression.png

🛠 Technologies Used
Python 3
Scikit-learn
Matplotlib


📂 Project Structure
linear_regression_house_price/
│
├── linear_regression_house_price.py
├── README.md
├── requirements.txt
├── .gitignore
└── images/
    └── linear_regression.png



🚀 How to Run
1. Navigate to the project
cd projects/linear_regression_house_price
2. Install dependencies
pip install -r requirements.txt
3. Run the program
python3 linear_regression_house_price.py


📖 Learning Outcomes

Through this project, I learned:

Linear Regression
Supervised Learning
Continuous numerical prediction
Features and target variables
Model training using fit()
Prediction using predict()
Slope / coefficient
Intercept
Best-fit regression line
Data visualization


🔮 Future Improvements
Use a larger real-world house price dataset.
Add multiple features such as location, number of bedrooms, and age of the house.
Split the dataset into training and testing sets.
Evaluate the model using regression metrics such as MAE, MSE, RMSE, and R².
Implement Multiple Linear Regression.


👨‍💻 Author

Jasim AG

GitHub:
https://github.com/Jasim-AG/ai-engineer-journey