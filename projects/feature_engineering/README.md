# 🛠️ Feature Engineering using Pandas

## 📌 Project Overview

This project demonstrates **Feature Engineering**, one of the most important steps in the Machine Learning pipeline.

Feature Engineering is the process of creating new features from existing data to improve the performance of Machine Learning models. Instead of only using the original dataset, we generate more meaningful features that help the model learn better patterns.

In this project, two new features (**Age** and **BMI**) are created from the existing dataset.

---

# 🎯 Objectives

* Understand Feature Engineering
* Create new features from existing data
* Calculate Age from Birth Year
* Calculate BMI using Height and Weight
* Learn why Feature Engineering improves Machine Learning models

---

# 🛠 Technologies Used

* Python 3
* Pandas

---

# 📂 Dataset

The sample dataset contains the following information:

| Birth Year | Height (cm) | Weight (kg) |
| ---------- | ----------: | ----------: |
| 2000       |         170 |          70 |
| 2002       |         160 |          55 |
| 1998       |         180 |          80 |

---

# 📚 Concepts Covered

## What is Feature Engineering?

Feature Engineering is the process of **creating, transforming, or selecting features** to improve the performance of a Machine Learning model.

Rather than changing the algorithm, we improve the quality of the input data.

---

## Features Created

### 1️⃣ Age

Age is calculated from the Birth Year.

```python
current_year = 2026

df["Age"] = current_year - df["Birth_Year"]
```

Example:

| Birth Year | Age |
| ---------- | --: |
| 2000       |  26 |
| 2002       |  24 |
| 1998       |  28 |

---

### 2️⃣ Body Mass Index (BMI)

BMI is calculated using Height and Weight.

Formula:

```text
BMI = Weight (kg) / Height (m)²
```

Since height is stored in **centimeters**, it is converted to **meters** before calculation.

```python
df["BMI"] = df["Weight"] / ((df["Height"] / 100) ** 2)
```

Example:

Height = **170 cm**

Weight = **70 kg**

BMI ≈ **24.22**

---

# 🚀 Workflow

1. Import Pandas
2. Create Dataset
3. Create DataFrame
4. Calculate Age
5. Calculate BMI
6. Display Updated Dataset

---

# 📂 Project Structure

```text
feature_engineering/
│
├── feature_engineering.py
├── README.md
└── requirements.txt
```

---

# 📊 Input Dataset

      name     weight  height  birth_year
0     jasii      80     175        2005
1     jusii      50     110        2000
2     riii       60     130        2009
3     ruaa        6      60        2024

---

# 📊 Output Dataset

   name     weight  height     birth_year  age       BMI
0  jasii      80     175        2005       21     0.002612
1  jusii      50     110        2000       26     0.004132
2   riii      60     130        2009       17     0.003550
3   ruaa       6      60        2024        2     0.001667

> **Note:** BMI values are rounded for readability.

---

# 💡 Why Feature Engineering?

Feature Engineering helps Machine Learning models by providing more meaningful information.

Examples:

* Birth Year → Age
* Height + Weight → BMI
* Purchase Date → Month, Day, Weekend
* Area + Bedrooms → Area per Bedroom

Better features often lead to better model performance.

---

# 📖 Key Learnings

* What Feature Engineering is
* Creating new features
* Calculating Age from Birth Year
* Calculating BMI from Height and Weight
* Improving data quality for Machine Learning

---

# 🎓 Skills Gained

* Feature Engineering
* Data Transformation
* Pandas DataFrame Operations
* Python Programming
* Machine Learning Data Preparation

---

# 📈 Future Improvements

* Date Feature Extraction
* Feature Selection
* One-Hot Encoding
* Polynomial Features
* Log Transformation
* Interaction Features

---

# 👨‍💻 Author

**Jasim**

B.Tech Computer Science Student

Passionate about Artificial Intelligence, Machine Learning, and building real-world AI projects.

---

## ⭐ Part of AI Engineer Journey

This project is part of my **AI Engineer Journey**, where I document my daily learning by building practical Machine Learning projects from scratch. The goal is to develop a strong foundation in AI through hands-on coding, professional documentation, and continuous learning.

---

## 📌 Interview Takeaway

**Q: What is Feature Engineering?**

**Answer:**

> Feature Engineering is the process of creating, transforming, or selecting features from existing data to improve the performance of a Machine Learning model. High-quality features often have a greater impact on model performance than simply changing the learning algorithm.
