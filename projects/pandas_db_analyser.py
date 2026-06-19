import pandas as pd
data = {
    "Name" : ["jasii", "ruaa", "john"],
    "Mark": [20, 80, 50]
}

df = pd.DataFrame(data)
print("Data is ", df)
print("highest mark is", df["Mark"].max())
print("lowest mark is",df["Mark"].min())
print("Avarage mark is", df["Mark"].mean())
print("name of student with mark greater or equal to 50 is",df[df["Mark"]>=80])