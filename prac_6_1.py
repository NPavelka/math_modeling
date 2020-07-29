print('-----------------------------Zadanie_1--------------------------------')
print('Функция, строящая графики кривых, заданных параметрически: Циклоиды и Астроиды')

import matplotlib.pyplot as plt 
import numpy as np

def cicloida(t=3, R=1, title='Crivai-cicloida'):
    """Функция строит циклоиду: кривая, описанная точкой, лежащей на окружности радиуса R, если эта окружность катится без скольжения по прямой.
       На вход подаются:
       t - кол-во дуг
       R - радиус окружности
       title - название кривой
    """
    
    if t <= 0:
        print('Задана неправильная t')
    
    t = np.arange(0, 2 * t * np.pi, 0.01)
    
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))

    plt.plot(x,y,color='g', label='Cicloida')
    
    plt.title('Cicloida')                           #Подпись графика
    plt.xlabel('Coord - x')                         #Подпись оси Ох
    plt.ylabel('Coord - y')                         #Подпись оси Оу
    plt.axis('equal')
    plt.grid()
    
    plt.show()

def astroida(t=3, R=1, title='Crivai-astroida'):
    """Функция строит астроиду: кривая, некоторой точки окружности радиуса R/4, катящейся без скольжения
       по другой окружности радиуса R причем меньшая оркужность все время остается внутри большей.
       На вход подаются:
       t - угол, который непонятно за что отвечает
       R - радиус окружности
       title - название кривой
    """
    
    if t <= 0:
        print('Задана неправильная t')
    
    t = np.arange(0, 2 * t * np.pi, 0.01)
    
    x = R * np.cos(t)**3
    y = R * np.sin(t)**3

    plt.plot(x,y,color='b', label='Astroida')
    
    plt.title('Astroida')                           #Подпись графика
    plt.xlabel('Coord - x')                         #Подпись оси Ох
    plt.ylabel('Coord - y')                         #Подпись оси Оу
    plt.axis('equal')
    plt.grid()
    
    plt.show()


cicloida(5,6)
astroida(10,10)