print('-----------------------------Zadanie_2--------------------------------')
print('Создание анимации круга расширяющегося радиуса.')

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as anim

#Создание пространства для анимации
fig, ax = plt.subplots(figsize=(8,8))

#Анимируемый объект
circle, = plt.plot([], [], color = 'r', label = 'Circle')

#Функция анимации окружности
def circle_func(r, t):
    """Функция создаёт анимацию расширения окружности.
       На вход подаются:
       r - радиус окружности
       t - коэфициент изменения радиуса окружности
    """
    alpha = np.linspace(0, 2 * np.pi, 30)
    
    R = r * t
    
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    
    return x, y

#Параметры анимации
N = 100                                      #Кол-во точек/кадров
ax.set_xlim(-100, 100)                       #Пределы изменения переменной X
ax.set_ylim(-100, 100)                       #Пределы изменения переменной Y  
plt.legend()

#Функция подстановки параметров
def animate(i):                                              
    circle.set_data(circle_func(r = 2, t = i))
    
#Анимация
ani = anim.FuncAnimation(fig, animate, frames = N, interval = 100)

ani.save('animation_7_2.gif')