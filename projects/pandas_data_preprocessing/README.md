# 📊 Pandas Data Preprocessing

## 📌 Project Overview

This project demonstrates the basic data preprocessing techniques used in Machine Learning using the Pandas library.

Data preprocessing is an essential step before training any Machine Learning model because real-world datasets often contain missing values, duplicate records, and inconsistent data.

---

## 🎯 Objectives

* Detect missing values
* Count missing values
* Remove missing values
* Fill missing values
* Detect duplicate records
* Remove duplicate records

---

## 🛠 Technologies Used

* Python 3
* Pandas

---

## 📂 Dataset

A sample dataset was created using Pandas DataFrame containing:

* Name
* Age
* Marks

The dataset intentionally includes:

* Missing values (NaN)
* Duplicate rows

to demonstrate preprocessing techniques.

---

## 📚 Concepts Covered

### 1. Finding Missing Values

```python
df.isnull()
```

Checks whether each value is missing.

---

### 2. Counting Missing Values

```python
df.isnull().sum()
```

Counts missing values in each column.

---

### 3. Counting Total Missing Values

```python
df.isnull().sum().sum()
```

Returns the total number of missing values in the dataset.

---

### 4. Removing Missing Values

```python
df.dropna()
```

Removes rows containing missing values.

---

### 5. Filling Missing Values

```python
df.fillna()
```

Replaces missing values with a specified value such as:

* Mean
* Median
* Mode
* Constant Value

Example:

```python
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

---

### 6. Removing Duplicate Rows

```python
df.drop_duplicates()
```

Removes duplicate records from the dataset.

---

## 🚀 Workflow

1. Import Pandas
2. Create Dataset
3. Check Missing Values
4. Count Missing Values
5. Remove Missing Values
6. Fill Missing Values
7. Detect Duplicate Rows
8. Remove Duplicate Rows

---

## 📁 Project Structure

```
pandas_data_preprocessing/
│
├── preprocessing.py
├── README.md
└── requirements.txt
```

---

## 📖 Key Learnings

* Importance of data preprocessing
* Handling missing values
* Difference between `dropna()` and `fillna()`
* Understanding duplicate records
* Using Pandas for data cleaning

---

## 🎓 Skills Gained

* Data Cleaning
* Data Inspection
* Pandas DataFrame Operations
* Machine Learning Data Preparation

---

## 📈 Future Improvements

* Label Encoding
* One-Hot Encoding
* Feature Scaling
* Outlier Detection
* Data Normalization
* Standardization

---

## 👨‍💻 Author

**Jasim**

B.Tech Computer Science Student

Learning AI & Machine Learning by building real-world projects.

---

⭐ This project is part of my **AI Engineer Journey**, where I document my daily learning, projects, and progress from Python fundamentals to advanced Artificial Intelligence.
