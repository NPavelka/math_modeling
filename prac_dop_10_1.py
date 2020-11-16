print('--------------------------------Dop_Zadanie_1-------------------------------')
print('Функция распределения частиц в кольце объекта')

#Подключение необходимых для программы библиотек
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from scipy.integrate import odeint

# Константы
G = 6.67 * 10**(-11)   #Гравитационная постоянная
M0 = 1.989 * 10**30

def func_object(r, N):
    #Создание таблицы с параметрами координат и скоростей объектов
    a = np.ndarray(shape=(N,4))

    #Создание цикла для определения координат и скоростей к заданному объекту
    for i in range(0, N, 1):

        #Определение угла для объектов
        alp = 2 * np.pi / N * i

        #Определение координат для первого кольца
        x = r * np.sin(alp)
        y = r * np.cos(alp)

        #Подставление координат в таблицу
        a[i, 0] = x
        a[i, 1] = y

        #Определение границ(для рис.1)
        plt.xlim(-2*r,2*r)
        plt.ylim(-2*r,2*r)

        #Определение размеров объектов (для рис.1)
#        ms = 2**(20/N) + 5

        #Создание маркеров объектов (для рис.1)
        plt.plot(x, y, marker='.', markersize=20)

        #Определение круговой скорости для объектов, вращающихся вокруг планеты
        Vc = np.sqrt(G * M0 / r)

        #Определение проекций скоростей в разных четвертях тригонометрической окружности для первого кольца
        #Первая четверть
        if x >= 0 and y >= 0:
            Vx = -Vc * np.cos(alp)
            Vy = Vc * np.sin(alp)

        #Вторая четверть
        elif x < 0 and y >= 0:
            Vx = -Vc * np.sin(alp-3*np.pi/2)
            Vy = -Vc * np.cos(alp-3*np.pi/2)

        #Третья четверть
        elif x < 0 and y < 0:
            Vx = -Vc * np.cos(alp)
            Vy = Vc * np.sin(alp)

        #Четвёртая четверть
        elif x >= 0 and y < 0:
            Vx = Vc * np.sin(alp-np.pi/2)
            Vy = Vc * np.cos(alp-np.pi/2)
        else:
            print('error')

        #Подставление проекций скоростей  в  таблицу
        a[i, 2] = Vx
        a[i, 3] = Vy
        
plt.axis('equal')
plt.grid()
func_object(100, 12)