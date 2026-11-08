arr=[2,6,4,9,2,4,9,1,3,5,7,8,0]
k=4
window_sum=sum(arr[:k])
max_sum=window_sum
for i in range(k,len(arr)):
    window_sum+=arr[i]
    window_sum-=arr[i-k]

    max_sum=max(max_sum,window_sum)
print("max sum = ",max_sum)
