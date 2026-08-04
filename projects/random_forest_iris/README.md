# 🌲 Random Forest - Iris Classification

A Machine Learning classification project that predicts the species of Iris flowers using the **Random Forest** algorithm from Scikit-learn.

---

## 📌 Project Overview

This project demonstrates how to build, train, and evaluate a **Random Forest Classifier** using the famous Iris dataset.

The model classifies Iris flowers into one of three species:

- Iris Setosa
- Iris Versicolor
- Iris Virginica

The project evaluates the model using:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 📂 Project Structure

```
random_forest_iris/
│
├── random_forest_iris.py
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

### Features

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

### Target Classes

- Iris Setosa
- Iris Versicolor
- Iris Virginica

---

## 🤖 Machine Learning Algorithm

Algorithm Used:

**Random Forest Classifier**

```python
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

Random Forest builds multiple decision trees using **bootstrap sampling** and **random feature selection**. The final prediction is made using **majority voting**.

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

---

## 🚀 How to Run

Clone the repository

```bash
git clone https://github.com/Jasim-AG/ai-engineer-journey.git
```

Navigate to the project

```bash
cd projects/random_forest_iris
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python3 random_forest_iris.py
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

- Random Forest Classifier
- Ensemble Learning
- Bootstrap Sampling
- Random Feature Selection
- Majority Voting
- Train-Test Split
- Accuracy Score
- Confusion Matrix
- Classification Report
- Git & GitHub Workflow

---

## 🔮 Future Improvements

- Hyperparameter Tuning
- Cross Validation
- Feature Importance Visualization
- Compare with Decision Tree
- Compare with SVM

---

## 👨‍💻 Author

**Jasim AG**

GitHub:

https://github.com/Jasim-AG

---

## ⭐ Repository

If you found this project useful, consider giving the repository a ⭐.