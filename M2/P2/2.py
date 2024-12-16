import numpy as np

matrix_a = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

matrix_b = np.array([[10, 20, 30],
                     [40, 50, 60],
                     [70, 80, 90]])

result = np.dot(matrix_a, matrix_b.T)
print(result)
