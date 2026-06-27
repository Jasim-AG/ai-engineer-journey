import pandas as pd
Data = {
    "Name": ["jasim", "jusii", "ruaa", "riii","jasim"],
    "Age": [10, None, 20, 30, 10],
    "Mark": [80, 20, 50, None, 80]
        
}

df = pd.DataFrame(Data)
print("table is \n", df)
print("\nis there any null values \n", df.isnull())
print("\ncount of null values is\n", df.isnull().sum())
df["Age"] = df["Age"].fillna(df["Age"].mean())
print("\nage is modified\n",df)
df = df.fillna(5)
print("\nupdated table \n", df)
df = df.drop_duplicates()
print("\ntable after preprocessing is \n",df)