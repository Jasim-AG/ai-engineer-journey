# Cross-Validation: K-Fold and Stratified K-Fold

## 📌 Project Overview

This project demonstrates two important model evaluation techniques in Machine Learning:

1. **K-Fold Cross-Validation**
2. **Stratified K-Fold Cross-Validation**

Both techniques are implemented using Python and Scikit-learn with the Iris dataset and a Decision Tree Classifier.

The main objective is to understand how cross-validation evaluates a machine learning model using multiple training and validation splits.

---

## 🎯 Objectives

- Understand the concept of Cross-Validation.
- Implement K-Fold Cross-Validation.
- Implement Stratified K-Fold Cross-Validation.
- Evaluate model performance using accuracy.
- Calculate mean accuracy and standard deviation.
- Understand the difference between K-Fold and Stratified K-Fold.

---

## 📂 Project Structure

```text
cross_validation/
│
├── kfold_demo.py
├── stratified_kfold_demo.py
├── README.md
└── requirements.txt
```

---

## 🧠 1. K-Fold Cross-Validation

K-Fold Cross-Validation is a model evaluation technique that divides a dataset into K equal-sized folds.

Each fold is used once for validation, while the remaining K-1 folds are used for training.

### Working Process

For K = 5:

1. Divide the dataset into five folds.
2. Use the first fold for validation and the remaining four for training.
3. Repeat the process using the second fold for validation.
4. Continue until all five folds have been used for validation.
5. Calculate the average performance score.

### Implementation

**File:** `kfold_demo.py`

The implementation uses:

- Iris dataset
- DecisionTreeClassifier
- KFold
- cross_val_score

The model is evaluated using accuracy across five folds.

---

## 🧠 2. Stratified K-Fold Cross-Validation

Stratified K-Fold is a variation of K-Fold Cross-Validation mainly used for classification problems.

Unlike ordinary K-Fold, Stratified K-Fold attempts to maintain the original class distribution in every fold.

For example, if a dataset contains:

- 80% Class A
- 20% Class B

Stratified K-Fold tries to preserve this distribution in each fold.

### Advantages

- Maintains class proportions across folds.
- Useful for imbalanced classification datasets.
- Provides more representative validation splits.

### Implementation

**File:** `stratified_kfold_demo.py`

The implementation uses:

- Iris dataset
- DecisionTreeClassifier
- StratifiedKFold
- cross_val_score

The model is evaluated using accuracy across five stratified folds.

---

## ⚖️ K-Fold vs Stratified K-Fold

| Feature | K-Fold | Stratified K-Fold |
|---|---|---|
| Data splitting | Divides data into K folds | Divides data into K folds while preserving class proportions |
| Class distribution | Not explicitly preserved | Approximately preserved |
| Main usage | General model evaluation | Classification problems |
| Imbalanced datasets | May produce unrepresentative folds | Usually more suitable |

---

## ⚙️ Technologies Used

- Python
- NumPy
- Scikit-learn

---

## 📦 Installation

Install the required libraries:

```bash
pip install numpy scikit-learn
```

Alternatively, install dependencies using:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Run K-Fold Cross-Validation

```bash
python kfold_demo.py
```

### Run Stratified K-Fold Cross-Validation

```bash
python stratified_kfold_demo.py
```

---

## 📊 Evaluation Metrics

Both implementations display:

- Individual fold accuracy scores.
- Mean accuracy.
- Standard deviation.

### Mean Accuracy

The average accuracy across all folds represents the model's overall cross-validation performance.

### Standard Deviation

Standard deviation indicates how much the scores vary across the folds.

A lower standard deviation generally indicates more consistent performance across the evaluated folds.

---

## ⚠️ Important Note: Data Leakage

Cross-validation should be performed using the training data when selecting or tuning a model.

The final test dataset should remain separate and untouched until the final model evaluation.

This helps prevent data leakage and provides a more reliable estimate of model performance.

---

## 📚 Key Learnings

- Understood the importance of Cross-Validation.
- Learned how K-Fold divides a dataset into multiple folds.
- Implemented K-Fold Cross-Validation using Scikit-learn.
- Learned how Stratified K-Fold maintains class proportions.
- Compared model performance using multiple validation folds.
- Understood mean accuracy and standard deviation.

---

## 👨‍💻 Author

**Jasim A G**

GitHub: [Jasim-AG](https://github.com/Jasim-AG)

Repository: [AI Engineer Journey](https://github.com/Jasim-AG/ai-engineer-journey)

**Learning Journey – Day 68**