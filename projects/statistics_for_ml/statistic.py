import numpy as np
from statistics import mode
data=[10,20,30,40,50]
print("statistics for ML")
print("_"*18)
print("data set is", data)
print("mean :", np.mean(data))
print("median :", np.median(data))
print("mode :", mode(data))
print("Variance :", np.var(data))
print("SD :", np.std(data))

print("\nInterpretation")
print("-" * 45)

if np.var(data) < 100:
    print("✔ Data is less spread.")
else:
    print("✔ Data is highly spread.")

print(f"✔ Most frequent value is {mode(data)}.")

if np.mean(data) > np.median(data):
    print("✔ Mean is greater than Median.")
elif np.mean(data) < np.median(data):
    print("✔ Median is greater than Mean.")
else:
    print("✔ Mean and Median are equal.")