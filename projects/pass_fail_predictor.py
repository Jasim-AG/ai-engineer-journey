from sklearn.linear_model import LogisticRegression
import numpy as np

hour = np.array([[1], [2], [3], [4], [5]])
result = np.array([0, 0, 0, 1, 1])
model = LogisticRegression()
model.fit(hour, result)
while True:
    k = input("enter the hour (enter q to quit):")
    if k == 'q':
        break
    else:
        k=int(k)
        prediction = model.predict([[k]])
        print("prediction is :",prediction[0])

