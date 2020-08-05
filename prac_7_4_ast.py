print('-----------------------------Zadanie_4--------------------------------')
print('Функция, строящая графики кривых, заданных параметрически: Циклоиды и Астроиды, а также анимирует движение точки по ним.')

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as anim    

#Создание пространства и подпространства для анимации 
fig, ax = plt.subplots(figsize=(8,8)) 
n = []              

#Создание анимируемого объкта
anim_object_1, = plt.plot([], [], color='b', label='Аstroida')
anim_object_2, = plt.plot([], [], color='r', label='Circle-inside')
anim_object_3, = plt.plot([], [], color='m', label='Circle-outside')
anim_object_4, = plt.plot([], [], marker = 'o', color='orange', ms=6, label='Point') 

#Координаты анимируемого объекта
xdata_1, ydata_1 = [], []
xdata_2, ydata_2 = [], []
xdata_3, ydata_3 = [], []
xdata_4, ydata_4 = [], [] 

def astroida_move(frame = None, R=8):
    """Функция строит астроиду с помощью окружности: кривая, описанная точкой, лежащей на окружности радиуса R, если эта окружность катится без скольжения по прямой.
       На вход подаются:
       R - радиус окружности
       frame - кадры
    """
    t = frame
    alpha = np.linspace(0, 2 * np.pi, 50)
    
    xdata_1.append(R * np.cos(t)**3)
    ydata_1.append(R * np.sin(t)**3)
    anim_object_1.set_data(xdata_1, ydata_1)
    
    xdata_2.append(3*R/4 * np.cos(t) + R/4 * np.cos(alpha))
    ydata_2.append(3*R/4 * np.sin(t) + R/4 * np.sin(alpha))    
    anim_object_2.set_data(xdata_2[len(n)-1], ydata_2[len(n)-1])
    
    xdata_3.append(R * np.cos(alpha))
    ydata_3.append(R * np.sin(alpha))    
    anim_object_3.set_data(xdata_3, ydata_3)
    
    xdata_4.append(R * np.cos(t)**3)
    ydata_4.append(R * np.sin(t)**3)
    anim_object_4.set_data(xdata_4[len(n)-1], ydata_4[len(n)-1])
    
    return anim_object_1, anim_object_2, anim_object_3, anim_object_4,
  
#Пределы изменения переменной X и Y
ax.set_xlim(-14, 14)  
ax.set_ylim(-14, 14)

animation_7_4 = anim.FuncAnimation(fig, astroida_move, frames = np.linspace(0, 6 * np.pi, 300), interval=1)

animation_7_4.save('animation_7_4_ast.gif')
