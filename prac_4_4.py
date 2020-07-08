print('-----------------------------Zadanie_4--------------------------------')
print('Фунуция вычисляет значения y = x**2 на промежутке a < x < b в N точках. Функция возвращает массив значений.')

import numpy as np

def prost_func(a, b, N):
    A = np.zeros((1,N))
    k = 0
    for i in np.linspace(a, b, N):
        A[0, k] = i**2
        k = k + 1
    print(A)
    
N = int(input('Введите кол-во чисел в последовательности: '))
a = int(input('Задайте начало ограничения: '))
b = int(input('Задайте конец ограничения: '))

prost_func(a, b, N)



