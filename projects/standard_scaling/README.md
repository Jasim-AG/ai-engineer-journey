# 📊 Standard Scaling using StandardScaler

## 📌 Project Overview

This project demonstrates **Feature Scaling** using **StandardScaler** from the Scikit-Learn library.

Standard Scaling is a data preprocessing technique that transforms numerical features so they have:

- **Mean ≈ 0**
- **Standard Deviation ≈ 1**

It is commonly used before training Machine Learning models, especially algorithms that are sensitive to the scale of data.

---

# 🎯 Objectives

- Understand Standard Scaling
- Learn why Feature Scaling is important
- Scale numerical features using StandardScaler
- Compare data before and after scaling
- Learn the difference between StandardScaler and MinMaxScaler

---

# 🛠 Technologies Used

- Python 3
- Pandas
- Scikit-Learn

---

# 📂 Dataset

A sample dataset containing employee salaries.

Example:

| Salary |
|--------:|
|30000|
|35000|
|40000|
|45000|
|5000000|

The dataset intentionally contains an **outlier** to demonstrate how StandardScaler behaves.

---

# 📚 Concepts Covered

## What is Standard Scaling?

Standard Scaling transforms data so that:

- Mean becomes approximately **0**
- Standard Deviation becomes approximately **1**

Unlike MinMaxScaler, StandardScaler does **not** scale values to the range **0–1**.

---

## Why Use StandardScaler?

Feature Scaling helps Machine Learning algorithms treat every feature fairly.

StandardScaler is commonly used when:

- Features have different numerical ranges.
- The dataset contains some outliers.
- Distance-based or optimization-based algorithms are used.

---

## What is an Outlier?

An outlier is a value that is significantly different from the rest of the data.

Example:

```text
10
11
12
13
500   ← Outlier
```

Outliers can influence data preprocessing and Machine Learning models.

---

# 🔧 Functions Used

## Import StandardScaler

```python
from sklearn.preprocessing import StandardScaler
```

---

## Create the Scaler

```python
scaler = StandardScaler()
```

---

## Learn and Scale the Data

```python
scaled_data = scaler.fit_transform(df)
```

This performs:

- Learning the data distribution
- Applying Standard Scaling

---

# 🚀 Workflow

1. Import Libraries
2. Create Dataset
3. Display Original Data
4. Create StandardScaler
5. Apply Standard Scaling
6. Display Scaled Data

---

# 📂 Project Structure

```
standard_scaling/
│
├── standard_scaling.py
├── README.md
└── requirements.txt
```

---

# 📖 Key Learnings

- Importance of Feature Scaling
- StandardScaler
- Mean and Standard Deviation
- Outliers
- Difference between MinMaxScaler and StandardScaler

---

# 📊 MinMaxScaler vs StandardScaler

| MinMaxScaler | StandardScaler |
|--------------|----------------|
| Output Range: **0–1** | Mean ≈ **0** |
| Uses Minimum & Maximum | Uses Mean & Standard Deviation |
| More sensitive to outliers | Generally a better choice when some outliers exist |

---

# 📸 Sample Output

### Before Scaling

| Salary |
|--------:|
|30000|
|35000|
|40000|
|45000|
|5000000|

### After Scaling

```text
      Salary
-0.50
-0.49
-0.49
-0.48
 1.96
```

> **Note:** The exact scaled values may vary depending on the dataset.

---

# 🎓 Skills Gained

- Data Preprocessing
- Feature Scaling
- StandardScaler
- Pandas
- Scikit-Learn
- Machine Learning Fundamentals

---

# 📈 Future Improvements

- RobustScaler
- Normalization
- Feature Engineering
- Outlier Detection
- Data Visualization

---

# 👨‍💻 Author

**Jasim**

B.Tech Computer Science Student

Currently learning Artificial Intelligence and Machine Learning through practical projects and daily coding.

---

## ⭐ Part of AI Engineer Journey

This project is part of my **AI Engineer Journey**, where I document my daily learning, practical implementations, and Machine Learning projects while building a strong foundation in Artificial Intelligence.