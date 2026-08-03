# ⚔️ Support Vector Machine (SVM) - Iris Classification

A Machine Learning classification project that predicts the species of Iris flowers using the **Support Vector Machine (SVM)** algorithm from Scikit-learn.

---

## 📌 Project Overview

This project demonstrates how to build, train, and evaluate a **Support Vector Machine (SVM)** classifier using the famous Iris dataset.

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
svm_iris_classification/
│
├── svm_iris.py
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

**Support Vector Machine (SVM)**

```python
model = SVC(kernel="linear")
```

The model learns the **optimal hyperplane** that maximizes the margin between different classes using **support vectors**.

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
cd projects/svm_iris_classification
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python3 svm_iris.py
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

- Support Vector Machine (SVM)
- Hyperplane
- Support Vectors
- Margin Maximization
- Linear Kernel
- Train-Test Split
- Accuracy Score
- Confusion Matrix
- Classification Report
- Git & GitHub Workflow

---

## 🔮 Future Improvements

- Experiment with RBF Kernel
- Compare Linear vs RBF Kernel
- Hyperparameter Tuning
- Cross Validation
- Compare SVM with KNN and Decision Tree

---

## 👨‍💻 Author

**Jasim AG**

GitHub:

https://github.com/Jasim-AG

---

## ⭐ Repository

If you found this project useful, consider giving the repository a ⭐.