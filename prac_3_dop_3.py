print('----------------------------Dop_Zadanie_3-----------------------------')
import numpy as np

M = int(input('Введите кол-во строк: '))
N = int(input('Введите кол-во столбцов: '))

A = np.ndarray(shape = (M, N))

print()

for k in range(0, M, 1):
    print('Заполните строку', k)
    for i in range(0, N, 1):
        if i < N:
            print('Введите ',i,'элемент столбца')
            A[k, i] = int(input())
        else:
             print('Строка заполнена')

print()
print('Полученный массив:')     
print(A)

l = 0

for k in range(0, N, 1):
    a = A[0,k]
    for i in range(0, M, 1):
        if A[i,l] > a:
            a = A[i,l]
    l = l + 1
    print('Максимальный элемент ',k,' столбца: ',a)