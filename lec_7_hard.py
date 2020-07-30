print('-------------------------------Аимация нестандартных объектов--------------------------------')
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.animation import FuncAnimation

#------------------------Создание пространства для анимации------------------------
fig, ax = plt.subplots(figsize=(10,3), facecolor='pink', frameon=True)

#------------------------Анимируемые объекты------------------------
circle, = plt.plot([], [], color = 'b', label = 'circle')

#------------------------Функции-генераторы параметров------------------------
def circle_func(R, x0, y0):
    alpha =np.linspace(0, 2 * np.pi, 30)
    x = x0 + R * np.cos(alpha)
    y = y0 + R * np.sin(alpha)
    return x, y

#------------------------Параметры анимации------------------------
N = 10                                  #Кол-во точек/кадров
ax.set_xlim(0, 10)                      #Пределы изменения переменной X
ax.set_ylim(0, 3)                       #Пределы изменения переменной Y  
plt.legend()
#plt.axis('equal')

#------------------------Функция подстановки параметров------------------------
def animate(i):                                              
    circle.set_data(circle_func(R = i/5, x0 = i, y0 = 1.5))
    
#------------------------Анимация------------------------
ani = FuncAnimation(fig, animate, frames = N, interval = 100)

ani.save('lec_7_hard-animation.gif')