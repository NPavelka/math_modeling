print('-----------------------------Zadanie_3--------------------------------')
print('Функция, строящая графики кривых, заданных параметрически: Циклоиды и Астроиды, а также анимирует движение точки по ним.')

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as anim                  

#Создание пространства и подпространства для анимации 
fig, ax = plt.subplots(figsize=(12,4))
n = []              

#Создание анимируемого объкта
anim_object_1, = plt.plot([], [], 'o',color='orange', ms=5, label='Cicloida')
anim_object_2, = plt.plot([], [], 'o', color='b', ms=4, label='Circle')
anim_object_3, = plt.plot([], [], marker = 'o', color='r', ms=7, label='Point')  

#Координаты анимируемого объекта
xdata_1, ydata_1 = [], []
xdata_2, ydata_2 = [], []
xdata_3, ydata_3 = [], []   

def cicloida_move(frame = None, R=2):
    """Функция строит циклоиду с помощью движения окружности с отмеченной точкой на ней.
       На вход подаются:
       frame - кадр
       R - радиус циклоиды
    """
    t = frame
    alpha = np.linspace(0, 2 * np.pi, 80)
    
    xdata_1.append(R * (t - np.sin(t)))
    ydata_1.append(R * (1 - np.cos(t)))
    anim_object_1.set_data(xdata_1, ydata_1)
   
    xdata_2.append(R*t + R * np.cos(alpha))
    ydata_2.append(R + R * np.sin(alpha))
    anim_object_2.set_data(xdata_2[len(n)-1], ydata_2[len(n)-1]) 
    
    xdata_3.append(R * (t - np.sin(t)))
    ydata_3.append(R * (1 - np.cos(t)))
    anim_object_3.set_data(xdata_3[len(n)-1], ydata_3[len(n)-1])

    return anim_object_1, anim_object_2, anim_object_3,

#Пределы изменения переменной X и Y
ax.set_xlim(-3, 41)  
ax.set_ylim(-3, 8)

animation_7_3 = anim.FuncAnimation(fig, cicloida_move, frames = np.linspace(0, 6 * np.pi, 300), interval=1)
    
animation_7_3.save('animation_7_3_cic.gif')
