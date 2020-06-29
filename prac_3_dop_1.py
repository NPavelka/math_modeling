print('----------------------------Dop_Zadanie_1-----------------------------')
import numpy as np

N = int(input('Введите кол-во строк: '))
M = int(input('Введите кол-во столбцов: '))

A = np.ndarray(shape = (N, M))

print()
print('Заполнение первого массива')

for k in range(0, M, 1):
    print('Заполните строку', k)
    for i in range(0, N, 1):
        if i < N:
            print('Введите ',i,'элемент столбца')
            A[k, i] = int(input())
        else:
             print('Строка заполнена')
     
print(A)

B = np.ndarray(shape = (N, M))


print('Заполнение второго массива')

for k in range(0, M, 1):
    print('Заполните строку', k)
    for i in range(0, N, 1):
        if i < N:
            print('Введите ',i,'элемент столбца')
            B[k, i] = int(input())
        else:
             print('Строка заполнена')
             
print(B)

print()
print('Вывод третьего массива')

C = np.ndarray(shape = (N, M))
for k in range(0, M, 1):
    for i in range(0, N, 1):
        if A[k,i] >= B[k,i]:
            C[k,i] = A[k,i]
        elif A[k,i] < B[k,i]:
            C[k,i] = B[k,i]

print(C)