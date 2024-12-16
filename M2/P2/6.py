import numpy as np

grades = np.array([75, 45, 60, 90, 30, 85, 40], dtype=float)

grades[grades > 50] *= 1.1

print(grades)
