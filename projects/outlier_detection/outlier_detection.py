import pandas as pd
data = {
    "age":[-5,10,12,15,25,100]
}
df = pd.DataFrame(data)
print(df)
q1 = df["age"].quantile(0.25)
q3 = df["age"].quantile(0.75)
iqr = q3 - q1
lower_limit = q1 - (iqr * 1.5)
upper_limit = q3 + (iqr * 1.5)
outlier = df[(df["age"] < lower_limit) | (df["age"] > upper_limit)]
print("outliers are \n", outlier)
