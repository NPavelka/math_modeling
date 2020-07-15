print('-----------------------------Dop_Zadanie_3--------------------------------')
print('Эллипс через полярные координаты')

import matplotlib.pyplot as plt 
import numpy as np

def func_graf(a = 2, b = 4, N=1000, title='Function'):
    """Функция строит график, где:
       a - начало ограничения
       b - конец ограничения
       N - кол-во точек в графике
       title - название кривой
    """
    plt.xlim(a-50, b+50)
    
    x = np.linspace(2*a, 2*b, N)
    y = np.zeros(N)
    
    for i in range(0,N,1):
        if x[i] < a:
            y[i] = a**2
        elif a <= x[i] and x[i] <= b:
            y[i] = x[i]**2
        elif x[i] > b:
            y[i] = b**2
    
    plt.plot(x, y, label='Linia', color='g')
    
    plt.grid()
    plt.title('Grafic')                            
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')

    plt.show()
    
func_graf(-20, 30, 1000)    
    
    
    