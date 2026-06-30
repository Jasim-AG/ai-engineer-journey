# 📦 Outlier Detection using IQR (Interquartile Range)

## 📌 Project Overview

This project demonstrates **Outlier Detection** using the **Interquartile Range (IQR)** method in Python with the Pandas library.

Outliers are data points that differ significantly from the rest of the dataset. Detecting and handling outliers is an important step in data preprocessing because they can negatively affect Machine Learning models and statistical analysis.

In this project, the IQR method is used to identify outliers automatically.

---

# 🎯 Objectives

* Understand what an outlier is
* Learn the IQR (Interquartile Range) method
* Calculate Quartiles (Q1 & Q3)
* Compute the IQR
* Determine Lower and Upper Limits
* Detect outliers using Python

---

# 🛠 Technologies Used

* Python 3
* Pandas

---

# 📂 Dataset

A sample dataset containing student marks.

Example:

| Marks |
| ----: |
|    65 |
|    70 |
|    72 |
|    68 |
|    69 |
|   250 |

The value **250** is intentionally added as an outlier for demonstration purposes.

---

# 📚 Concepts Covered

## What is an Outlier?

An outlier is a data point that is significantly different from the rest of the dataset.

Example:

```text
10
11
12
13
200   ← Outlier
```

Outliers may occur because of:

* Data entry mistakes
* Measurement errors
* Sensor failures
* Genuine rare observations

---

## What is IQR?

IQR stands for **Interquartile Range**.

It measures the spread of the middle 50% of the data.

Formula:

```text
IQR = Q3 - Q1
```

Where:

* **Q1** = First Quartile (25th Percentile)
* **Q3** = Third Quartile (75th Percentile)

---

## Outlier Detection Formula

### Lower Limit

```text
Lower Limit = Q1 - (1.5 × IQR)
```

### Upper Limit

```text
Upper Limit = Q3 + (1.5 × IQR)
```

Any value outside these limits is considered a **potential outlier**.

---

# 🔧 Functions Used

## Calculate First Quartile

```python
Q1 = df["Marks"].quantile(0.25)
```

---

## Calculate Third Quartile

```python
Q3 = df["Marks"].quantile(0.75)
```

---

## Calculate IQR

```python
IQR = Q3 - Q1
```

---

## Calculate Limits

```python
lower_limit = Q1 - (1.5 * IQR)

upper_limit = Q3 + (1.5 * IQR)
```

---

## Detect Outliers

```python
outliers = df[(df["Marks"] < lower_limit) | (df["Marks"] > upper_limit)]
```

---

# 🚀 Workflow

1. Import Pandas
2. Create Dataset
3. Calculate Q1
4. Calculate Q3
5. Compute IQR
6. Calculate Lower & Upper Limits
7. Detect Outliers
8. Display Outliers

---

# 📂 Project Structure

```text
outlier_detection/
│
├── outlier_detection.py
├── README.md
└── requirements.txt
```

---

# 📊 Sample Dataset

   AGE
   -5
   10
   12
   15
   25
  100
---

# 📊 Sample Output

```
Q1 = 10.5
Q3 = 22.5
IQR = Q3 - Q1
     = 22.5 - 10.5
     = 12
Upper_Limit=-7.5
Lower_Limit=40.5

output: 100    
```

> **Note:** The exact values may vary depending on the dataset.

---

# 💡 Why is Outlier Detection Important?

Outliers can:

* Reduce model accuracy
* Affect statistical calculations
* Mislead Machine Learning algorithms
* Distort visualizations

However, not every outlier should be removed.

Always investigate whether it is:

* A data error
* A measurement mistake
* A genuine rare observation

---

# 📖 Key Learnings

* What an outlier is
* IQR (Interquartile Range)
* Quartiles (Q1 & Q3)
* Detecting outliers using Python
* Importance of investigating outliers before removing them

---

# 🎓 Skills Gained

* Data Preprocessing
* Outlier Detection
* Pandas
* Statistical Analysis
* Machine Learning Data Preparation

---

# 📈 Future Improvements

* Z-Score Method
* Box Plot Visualization
* Outlier Removal
* Outlier Imputation
* RobustScaler
* Real-world Dataset Analysis

---

# 👨‍💻 Author

**Jasim**

B.Tech Computer Science Student

Learning Artificial Intelligence and Machine Learning through hands-on projects and continuous practice.

---

## ⭐ Part of AI Engineer Journey

This project is part of my **AI Engineer Journey**, where I build practical Machine Learning projects while learning core AI concepts. Each project focuses on solving a real data preprocessing or Machine Learning problem and is documented professionally to build a strong developer portfolio.

---

# 📌 Interview Takeaway

**Q: What is an outlier?**

**Answer:**

> An outlier is a data point that differs significantly from the rest of the dataset. It may occur due to data entry errors, measurement issues, or genuine rare observations.

---

**Q: Should all outliers be removed?**

**Answer:**

> No. Outliers should first be investigated. Impossible or erroneous values should be corrected or removed, while genuine rare observations should usually be retained.

---

**Q: What is IQR?**

**Answer:**

> IQR (Interquartile Range) is a statistical measure used to detect outliers. It is calculated as the difference between the third quartile (Q3) and the first quartile (Q1). Values outside the lower and upper limits calculated using IQR are considered potential outliers.
