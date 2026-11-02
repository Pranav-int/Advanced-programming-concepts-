import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print("Array: ",arr)
even=arr[arr%2==0]
odd=arr[arr%2!=0]

print("Even: ",even)
print("Odd: ",odd)