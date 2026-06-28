from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd

data = {
    "salary": [10000, 20000, 30000, 30000],
    "experiance":[2,4,6,8]
}
df = pd.DataFrame(data)
print("table before scaling\n", df)

scaler = MinMaxScaler()
scaled_data= scaler.fit_transform(df)
scaled_df =pd.DataFrame(scaled_data,columns=df.columns) 
print("\ntable after scaling\n", scaled_df)
