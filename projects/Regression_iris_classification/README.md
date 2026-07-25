# 📈 Logistic Regression - Iris Classification

A Machine Learning classification project that predicts the species of Iris flowers using the **Logistic Regression** algorithm from Scikit-learn.

---

## 📌 Project Overview

This project demonstrates how to build, train, and evaluate a **Logistic Regression** classifier using the famous Iris dataset.

The model classifies Iris flowers into one of three species:

- Iris Setosa
- Iris Versicolor
- Iris Virginica

The project also evaluates the model using:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 📂 Project Structure

```
logistic_regression_iris/
│
├── logistic_regression_iris.py
├── README.md
├── requirements.txt
├── .gitignore
└── images/
    └── output.png
```

---

## 🛠 Technologies Used

- Python 3
- Scikit-learn
- NumPy
- Matplotlib

---

## 📚 Dataset

**Dataset:** Iris Dataset

Source:

https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

Features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Target Classes:

- Iris Setosa
- Iris Versicolor
- Iris Virginica

---

## 🤖 Machine Learning Algorithm

Algorithm Used:

**Logistic Regression**

```python
model = LogisticRegression(max_iter=200)
```

The model predicts the probability of each class and assigns the class with the highest probability.

---

## 📊 Model Evaluation

The project evaluates the model using:

- Accuracy Score
- Confusion Matrix
- Classification Report

Example Output:

```
Accuracy : 100.00%
```

Confusion Matrix:

```
[[10 0 0]
 [0 9 0]
 [0 0 11]]
```

---

## 🚀 How to Run

Clone the repository

```bash
git clone https://github.com/Jasim-AG/ai-engineer-journey.git
```

Navigate to the project

```bash
cd projects/logistic_regression_iris
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the program

```bash
python3 logistic_regression_iris.py
```

---

## 📷 Output

Place the output screenshot inside:

```
images/output.png
```

---

## 📖 Learning Outcomes

After completing this project, I learned:

- Logistic Regression
- Binary & Multi-class Classification
- Sigmoid Function
- Probability Prediction
- Decision Boundary
- Train-Test Split
- Accuracy Score
- Confusion Matrix
- Classification Report
- Git & GitHub Project Management

---

## 🔮 Future Improvements

- Hyperparameter Tuning
- Cross Validation
- Feature Scaling
- Compare with Decision Tree and KNN
- Data Visualization

---

## 👨‍💻 Author

**Jasim AG**

GitHub:

https://github.com/Jasim-AG

---

## ⭐ Repository

If you found this project useful, consider giving the repository a ⭐.