import numpy as np

a = np.arange(1,10)
b = np.arange(11,20)

narr1 = a + b
narr2 = a - b
narr3 = a * b
narr4 = a / b

print(narr1)
print(narr2)
print(narr3)
print(narr4)

arr1 = np.arange(1,10)
arr2 = np.arange(11,20)
print(np.dot(arr1, arr2))
arr3 = np.array([arr1,arr2])

print(np.dot(arr3, arr3.T))
#Transpose

arr4 = np.arange(32).reshape(4,8)
arr5 = np.arange(32).reshape(8,4)

print(np.dot(arr4,arr5))