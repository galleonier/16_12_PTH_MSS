import numpy as np

data = np.array([
    ['Анна', 19, 'F', 1, 4.5],
    ['Борис', 21, 'M', 2, 3.7],
    ['Вера', 21, 'F', 3, 4.8],
    ['Глеб', 22, 'M', 4, 3.9],
    ['Дарья', 18, 'F', 1, 4.2],
    ['Егор', 23, 'M', 3, 4.1],
    ['Жанна', 21, 'F', 2, 4.6],
    ['Захар', 19, 'M', 1, 4.0]
])

mask = (data[:, 1].astype(int) > 20) & (data[:, 2] == 'F') & (data[:, 3].astype(int) == 3)
filtered_data = data[mask]

print(filtered_data)
