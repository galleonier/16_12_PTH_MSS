import numpy as np

arr1 = np.array([1, -2, 3, -4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

result = np.where(arr1 > 0, arr1, arr2)

print(result)
