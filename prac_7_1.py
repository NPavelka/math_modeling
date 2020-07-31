print('-----------------------------Zadanie_1--------------------------------')
print('Создание анимации движения окружности, заданного радиуса R, центр которой движется по параболе.')

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as anim    

#Создание пространства для анимации
fig, ax = plt.subplots(figsize=(5,8))

#Анимируемый объект
circle, = plt.plot([], [], color = 'b', label = 'Circle')

#Функция анимации окружности
def circle_func(R, x0, a, b, c):
    """Функция создаёт анимацию движения окружности, заданного радиуса R, центр которой движется по параболе.
       На вход подаются:
       R - радиус
       x0 - координата х
       a, b, c - параметры для построения параболы
    """
    alpha = np.linspace(0, 2 * np.pi, 30)
    
    y0 = a * x0**2 + b * x0 + c
    
    x = x0 + R * np.cos(alpha)
    y = y0 + R * np.sin(alpha)
    
    return x, y

#Функция параболы
def parabola(x0, a, b, c):
    y0 = a * x0**2 + b * x0 + c
    return x0, y0

#Функция подстановки параметров
def animate(i):                                              
    circle.set_data(circle_func(R = 0.5, x0 = i, a = 1, b = -8, c = 4))

#Создание параболы
sub = parabola(x0 = np.linspace(-2, 9, 100),a = 1, b = -8, c = 4)
plt.plot(sub[0],sub[1], color = 'g', label = 'Parabola')

#Украшательства
N = 100                                   #Кол-во точек/кадров
ax.set_xlim(-1, 9)                        #Пределы изменения переменной X
ax.set_ylim(-12, 4)                       #Пределы изменения переменной Y  
plt.legend()
plt.grid()

#Анимация
ani = anim.FuncAnimation(fig, animate, frames = N, interval = 600)

ani.save('animation_7_1.gif')