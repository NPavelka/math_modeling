print('-----------------------------Dop_Zadanie_1--------------------------------')
print('Кривые Лиссажу')

import matplotlib.pyplot as plt 
import numpy as np

def lissazhu(a=1, b=1, A=1, B=1, d=1, title='Lissajous curves'):
    """Функция строит кривые Лиссажу, где:
       a, b - частоты колебаний (возьмите значения a = 1, b - такие значения, чтобы b / a (или a / b) было натуральным числом. Например, b = 0.5, 0.25, 1, 2...)
       A, B - амплитуды (возьмите значения A = 1, B - произвольно)
       d - фаза (возьмите значение pi/2)
       title - название кривой
    """
    t = np.arange(0, 100, 0.01)
    
    x = A * np.sin(a * t + d)
    y = B * np.sin(b * t)
    
    plt.plot(x, y, label='Lissajous curves', color='orange')
    
    plt.grid()
    plt.title('Lissajous curves')                            
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')
    
    plt.show()
#--------a---b---A---B---d-------    
lissazhu(1, 0.8, 1, 6, np.pi/2)      