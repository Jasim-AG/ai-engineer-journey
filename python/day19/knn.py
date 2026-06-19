from sklearn.neighbors import KNeighborsClassifier
import numpy as np

hours = np.array([[1], [2], [3], [4], [5], [6], [7]])
result = np.array([0, 0, 0, 1, 1, 1, 1,])
model = KNeighborsClassifier(n_neighbors=3)
model.fit(hours, result)
while True:
    p=input("enter the hour (q for quit) :")
    if p == 'q':
        break
    else:
        prediction=model.predict([[int(p)]])
        print("prediction is :",prediction[0])

