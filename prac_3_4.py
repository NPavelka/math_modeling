print('-----------------------------Zadanie_4--------------------------------')

import numpy as np

N = int(input('Введите кол-во строк: '))
M = int(input('Введите кол-во столбцов: '))

A = np.ndarray(shape = (N, M))

print()
print('Заполнение массива')
print()

   
for i in range(0, N, 1):
    for j in range(0, M, 1):
        if j == 0 or i == 0: 
            A[i, j] = np.sin(N * (i + 1) + M * (j + 1))
        else:
            A[i, j] = np.sin(N * i + M * j)
  
for i in range(0, N, 1):
    for j in range(0, M, 1):
        if A[i,j] < 0:
            A[i, j] = 0

print(A)