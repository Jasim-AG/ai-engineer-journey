import pandas as pd

data = {
    "name": ["jasii", "jusii", "riii", "ruaa"],
    "weight": [80, 50, 60, 6],
    "height": [175, 110, 130, 60],
    "birth_year": [2005, 2000, 2009, 2024],
    
}
df = pd.DataFrame(data)
print("data table is \n", df)
curr_year = 2026
df["age"] = curr_year - df["birth_year"]
df["BMI"] = df["weight"] / ((df["height"]/100)** 2)
print("\nTable after feature engineering is\n", df)
