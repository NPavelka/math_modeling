print('-----------------------------Zadanie_2--------------------------------')
print('Функция, строящая графики кривых второго порядка, заданных явно: параболы и гиперболы')

import matplotlib.pyplot as plt 
import numpy as np

def hyperbola(x_lim=10, y_lim=10, N=100, a=1, b=1, title='Crivai-hyperbola'):
    """Функция строит гиперболу. На вход подаются:
       x_lim, y_lim - пределы графика
       N - кол-во точек
       a, b - необходимые параметры для создания кривой
       title - название кривой
    """
    plt.xlim(-x_lim, x_lim)
    plt.ylim(-y_lim, y_lim)
    
    x = np.linspace(-x_lim, x_lim, N)
    
    y = ((b**2)*((x**2)/(a**2)-1))**0.5
    plt.plot(x,y,color='b', label='Giperbola')
    y = -((b**2)*((x**2)/(a**2)-1))**0.5
    plt.plot(x,y,color='r', label='Giperbola')
    
    plt.title('Giperbola')                          #Подпись графика
    plt.xlabel('Coord - x')                         #Подпись оси Ох
    plt.ylabel('Coord - y')                         #Подпись оси Оу
    plt.grid() 
    
    plt.show()    

def parabola(x_lim=10, y_lim=10, N=100, a=1, b=1, c=1, title='Crivai-parabola'):
    """Функция строит параболу. На вход подаются:
       x_lim, y_lim - пределы графика
       N - кол-во точек
       a, b, c - необходимые параметры для создания кривой
       title - название кривой
    """
    plt.xlim(-2*x_lim, 2*x_lim)
    plt.ylim(-2*y_lim, 2*y_lim)
    
    x = np.linspace(-x_lim, x_lim, N)

    y = a * x**2 + b * x + c
    plt.plot(x,y,color='g', label='Parabola')
    
    plt.title('Parabola')                          #Подпись графика
    plt.xlabel('Coord - x')                         #Подпись оси Ох
    plt.ylabel('Coord - y')                         #Подпись оси Оу
    plt.grid()
    
    plt.show()
    
hyperbola(10,10,10000,4,5)

print('-----------------------------------------------------------------------') 

parabola(10,10,10000,1,8,2)    
  
    
    
    
    