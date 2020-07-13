print('-----------------------------Zadanie_3--------------------------------')
print('Функция, строящая графики кривых второго порядка, заданных неявно: окружности и эллипса')

import matplotlib.pyplot as plt 
import numpy as np

def circle(x_lim=10, y_lim=10, N=100, R=1, title='Circle-plotter'):
    """Функция строит окружность. На вход подаются:
       x_lim, y_lim - пределы графика
       N - кол-во точек
       R - радиус окружности
       title - название кривой
    """
    plt.xlim(-x_lim, x_lim)
    plt.ylim(-y_lim, y_lim)
    
    x = np.linspace(-2*R, 2*R, N)
    y = np.linspace(-2*R, 2*R, N)
    
    X, Y = np.meshgrid(x, y)                        #Указание на неявное задание координат
    fxy = X**2 + Y**2                               #Уравнение кривой
    
    plt.contour(X, Y, fxy, levels=[R**2])           #Команда рисования неявнозаданных кривых
    
    plt.grid()
    plt.title('Circle')                             #Подпись графика
    plt.xlabel('Coord - x')                         #Подпись оси Ох
    plt.ylabel('Coord - y')                         #Подпись оси Оу
    plt.axis('equal')  
    
    plt.show()

def ellipse(x_lim=10, y_lim=10, N=100, a=1, b=1, title='Crivai-ellipse'):
    """Функция строит эллипс. На вход подаются:
       x_lim, y_lim - пределы графика
       N - кол-во точек
       a, b - необходимые параметры для создания кривой
       title - название кривой
    """
    plt.xlim(-x_lim, x_lim)
    plt.ylim(-y_lim, y_lim)
    
    x = np.linspace(-x_lim, x_lim, N)
    y = np.linspace(-y_lim, y_lim, N)
    
    X, Y = np.meshgrid(x, y)
    fxy = X**2 / a**2 + Y**2 / b**2
    
    plt.contour(X, Y, fxy, levels=[1]) 
    
    plt.grid()
    plt.title('Ellipse')                            #Подпись графика
    plt.xlabel('Coord - x')                         #Подпись оси Ох
    plt.ylabel('Coord - y')                         #Подпись оси Оу
    plt.axis('equal')  
    plt.show()
    
circle(10,10,1000,2)

print('------------------------------------------------------------------------')

ellipse(10,10,1000,7,5)