from sklearn.linear_model import LinearRegression
import numpy as np

hour = np.array([[1], [2], [3], [4], [5]])
mark = np.array([35, 45, 55, 65, 75])
model = LinearRegression()
model.fit(hour, mark)
while True:
    k = input("enter the hour (or q to quit):")
    if k == 'q':
        break
    else:
        predict = model.predict([[int(k)]])
        print("predicted mark is :", round(predict[0], 2))

