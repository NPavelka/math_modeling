print('----------------------------Dop_Zadanie_5-----------------------------')
print('Вывод простых множителей числа')

n = int(input('Введите число: ' ))

while n > 1:
    d = 2
    stop = 0
    
    while stop != 1:
        if n % d == 0:
            n = n // d
            print(d, end = ' ')
            stop = 1
            
        else:
            d = d + 1
            
    if stop == 1:
        continue            
