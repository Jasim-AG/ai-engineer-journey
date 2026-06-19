from sklearn.model_selection import train_test_split
import numpy as np

x = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
x_train, y_train, x_test, y_test = train_test_split(x, y, test_size=0.2)
print("training data :")
print(x_train)
print()
print("test data")

print(x_test)
