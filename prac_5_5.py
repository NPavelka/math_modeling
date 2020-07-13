print('-----------------------------Zadanie_3--------------------------------')
print('Функция, строящая графики кривых второго порядка, заданных неявно: окружности и эллипса')

import matplotlib.pyplot as plt 
import numpy as np

def log_spiral(b=1, title='Log_Spiral'):
    """Функция строит логарифмическую спираль. На вход подаются:
       b - необходимые параметры для создания кривой
       title - название кривой
    """      
    f = np.arange(0, 8* np.pi, 0.01)
    
    x = np.cos(f) * np.e**(b * f)
    y = np.sin(f) * np.e**(b * f)
    
    plt.plot(x, y, label='Log_Spiral', color='b')
    plt.grid()
    plt.title('Log_Spiral')                            
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')
    
    plt.show()

def arhim_spiral(k=1, title='Arhimed_Spiral'):
    """Функция строит логарифмическую спираль. На вход подаются:
       k - необходимые параметры для создания кривой
       title - название кривой
    """ 
    f = np.arange(0, 8* np.pi, 0.01)
    
    x = np.cos(f) * k * f
    y = np.sin(f) * k * f
    
    plt.plot(x, y, label='Arhimed_Spiral', color='y')
    
    plt.grid()
    plt.title('Arhimed_Spiral')                            
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')
    
    plt.show()
    
def spiral_zhezl(k=1, title='Spiral_baton'):
    """Функция строит спираль-жезл. На вход подаются:
       k - необходимые параметры для создания кривой
       title - название кривой
    """ 
    f = np.arange(0.01, 8* np.pi, 0.01)
    
    x = np.cos(f) * k / f**0.5
    y = np.sin(f) * k / f**0.5
    
    plt.plot(x, y, label='Spiral_Baton', color='g')
    plt.grid()
    plt.title('Spiral_Baton')                            
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')
    
    plt.show()

def rosa_spiral(k=1, title='Rosa'):
    """Функция строит розу. На вход подаются:
       k - необходимые параметры для создания кривой
       title - название кривой
    """ 
    f = np.arange(0, 8* np.pi, 0.01)
    
    x = np.cos(f) * np.sin(k * f)
    y = np.sin(f) * np.sin(k * f)

    plt.plot(x, y, label='Rosa', color='r')
    plt.grid()
    plt.title('Rosa')                            
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')
    
    plt.show()
 
log_spiral(0.2)
arhim_spiral(10)
spiral_zhezl(1)    
rosa_spiral(4)    