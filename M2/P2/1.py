import numpy as np

arr1 = np.arange(1, 13).reshape(3, 4)
arr2 = np.tile([2, 3, 4, 5], 3).reshape(3, 4)

print("Сложение матриц:\n", arr1 + arr2)
print("Вычитание матриц:\n", arr1 - arr2)
print("Умножение матриц:\n", arr1 * arr2)
print("Возведение в квадрат arr1:\n", arr1 ** 2)
print("Увеличение на 50% arr2:\n", arr2 * 1.5)
