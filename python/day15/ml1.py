from sklearn.linear_model import LinearRegression
import numpy as np
 
x = np.array([[1], [2], [3], [4], [5]])
y = np.array([40, 50, 60, 70, 80])
model = LinearRegression()
model.fit(x, y)
prediction=model.predict([[6]])
print("predicted mark :", prediction[0])
