print('----------------------------Dop_Zadanie_1-----------------------------')
print('Функция возведения числа в степень')

def stepen(a = float(input('Введите число, которое возводится в степень: ')),
           n = int(input('Введите степень числа: '))):
    """ Функция возведения числа в степень
    """
    d = 1
    for i in range(0, n, 1):
        d = a * d
    print(d)
    return a

stepen()
