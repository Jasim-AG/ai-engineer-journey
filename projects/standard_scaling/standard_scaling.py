from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd

data = {
    "salary": [30000, 35000, 40000, 45000, 5000000]
    
}
df = pd.DataFrame(data)
print("table before scaling\n", df)

scaler = StandardScaler()
scaled_data= scaler.fit_transform(df)
scaled_df =pd.DataFrame(scaled_data,columns=df.columns) 
print("\ntable after scaling\n", scaled_df)
