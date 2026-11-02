import numpy as np
m=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(m)
print("First row:",m[0])
print("Last column:",m[:,-1])
print("Diagonal elements:",np.diag(m))
print("Second and third rows:",m[1:3])