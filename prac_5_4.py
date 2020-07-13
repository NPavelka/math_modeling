print('-----------------------------Zadanie_4--------------------------------')
print('Функция рисует лесенку')

import matplotlib.pyplot as plt 

def lesenka(N, title='Lesenka'):
    """Функция строит лесенку. На вход подаются:
       N - кол-во ступенек
       title - название кривой
    """
    x = [0]
    y = [0]
    k = 1
    
    for i in range(0, 2*N, 1):
        if i % 2 == 0:
            x.append(k-1)
            y.append(k)
        elif i % 2 == 1:
            x.append(k)
            y.append(k)
            k = k + 1
    
    plt.plot(x, y, color='b')
    
    plt.title('Stairs')                          #Подпись графика
    plt.xlabel('Dlina')                          #Подпись оси Ох
    plt.ylabel('Vysota')                         #Подпись оси Оу
    plt.grid()
    
    plt.show()
       
lesenka(10)