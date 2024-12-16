import numpy as np

arr = np.array([1, -2, 0, 3, -4])

result = np.where(arr > 0, 'positive', 'non-positive')

print(result)
