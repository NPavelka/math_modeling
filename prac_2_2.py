print('-----------------------------Zadanie_2--------------------------------')
print('Создание геометрической прогрессии')

b = int(input('Введите первый член прогрессии: '))
q = int(input('Введите знаменатель прогрессии: '))
n = int(input('Кол-во чисел в прогресии: '))

for n in range(1, n+1, 1):
    B = b * q**(n - 1)
    print(B)