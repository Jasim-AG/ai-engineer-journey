
from sklearn.tree import DecisionTreeClassifier
import numpy as np

hour = np.array([[1], [2], [3], [4], [5]])
result = np.array([0, 0, 0, 1, 1])
model = DecisionTreeClassifier()
model.fit(hour, result)

while True:
    k = input("\nenter the hour(q fir quit) :")
    if k == 'q':
        break
    else:
        prediction = model.predict([[int(k)]])
        if prediction == 0:
            print("\nfail")
        else:
            print("\npass")
            