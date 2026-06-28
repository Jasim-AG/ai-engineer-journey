# 📏 Feature Scaling using MinMaxScaler

## 📌 Project Overview

This project demonstrates **Feature Scaling** using **MinMaxScaler** from Scikit-Learn.

Feature Scaling is a data preprocessing technique used to bring numerical features to a similar scale before training Machine Learning models.

Some Machine Learning algorithms, such as **K-Nearest Neighbors (KNN)** and **Support Vector Machine (SVM)**, rely on distance calculations. Without feature scaling, features with larger numerical values can dominate the model and produce poor results.

---

# 🎯 Objectives

- Understand why Feature Scaling is needed
- Learn how MinMaxScaler works
- Scale numerical features between **0 and 1**
- Compare data before and after scaling
- Learn the difference between `fit()`, `transform()`, and `fit_transform()`

---

# 🛠 Technologies Used

- Python 3
- Pandas
- Scikit-Learn

---

# 📂 Dataset

A sample dataset is created using Pandas containing:

- Salary
- Experience

Example:

| Salary | Experience |
|--------:|-----------:|
| 10000 | 2 |
| 20000 | 4 |
| 30000 | 6 |
| 30000 | 8 |

---

# 📚 Concepts Covered

## What is Feature Scaling?

Feature Scaling is the process of converting numerical features into a similar scale so that Machine Learning algorithms treat every feature fairly.

---

## Why is Feature Scaling Important?

Without scaling:

- Features with larger values dominate distance calculations.
- Distance-based algorithms may produce poor predictions.

With scaling:

- All numerical features contribute fairly.
- Model performance often improves.

---

## Algorithms That Need Feature Scaling

- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Logistic Regression
- K-Means Clustering

---

## Algorithms That Usually Do Not Need Feature Scaling

- Decision Tree
- Random Forest

---

# 🧠 MinMaxScaler

MinMaxScaler converts feature values into the range:

```text
0 → 1
```

Example:

| Original Salary | Scaled Salary |
|----------------:|--------------:|
|10000|0.0|
|20000|0.5|
|30000|1.0|

---

# 🔧 Functions Used

## Creating the Scaler

```python
scaler = MinMaxScaler()
```

---

## Learning the Feature Range

```python
scaler.fit(data)
```

The scaler learns:

- Minimum value
- Maximum value

---

## Applying Scaling

```python
scaler.transform(data)
```

Applies the learned scaling to the dataset.

---

## Learning and Applying Together

```python
scaler.fit_transform(data)
```

Equivalent to:

```python
scaler.fit(data)
scaler.transform(data)
```

---

# 🚀 Workflow

1. Import Libraries
2. Create Dataset
3. Display Original Data
4. Create MinMaxScaler
5. Scale Dataset
6. Display Scaled Data

---

# 📂 Project Structure

```
feature_scaling/
│
├── feature_scaling.py
├── README.md
└── requirements.txt
```

---

# 📖 Key Learnings

- Importance of Feature Scaling
- MinMaxScaler
- Difference between `fit()`, `transform()`, and `fit_transform()`
- Distance-based algorithms require scaling
- Decision Trees usually do not require scaling

---

# 📈 Future Improvements

- StandardScaler
- RobustScaler
- Normalization
- Feature Engineering
- Data Visualization Before & After Scaling

---

# 🎓 Skills Gained

- Data Preprocessing
- Feature Scaling
- Pandas
- Scikit-Learn
- Machine Learning Fundamentals

---

## 📸 Sample Output

### Before Scaling

| Salary | Experience |
|--------:|-----------:|
|10000|2|
|20000|4|
|30000|6|
|30000|8|

### After Scaling

| Salary | Experience |
|--------:|-----------:|
|0.00|0.00|
|0.50|0.33|
|1.00|0.67|
|1.00|1.00|

# 👨‍💻 Author

**Jasim**

B.Tech Computer Science Student

Currently learning Artificial Intelligence and Machine Learning by building real-world projects.

---

## ⭐ Part of AI Engineer Journey

This project is part of my **AI Engineer Journey**, where I document my daily progress, projects, and practical implementations while learning Python, Machine Learning, Deep Learning, and Artificial Intelligence.