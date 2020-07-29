print('-----------------------------Zadanie_4/2--------------------------------')
print('Функция рисует сердце.')

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as anim                  

#Создание пространства и подпространства для анимации 
fig, ax = plt.subplots()                                                                               

#Создание анимируемого объкта
anim_object, = plt.plot([], [], marker='o', color='red', ms=10, label='Heart')                  

#Координаты анимируемого объекта
xdata, ydata = [], []                                          

def heart_move(frame=None):
    """Функция рисует бабочку.
       На вход подаются:
       frame - количество кадров в секунду
    """
    xdata.append(16 * np.sin(frame)**3)
    ydata.append(13 * np.cos(frame) - 5 * np.cos(2 * frame) - 2 * np.cos(3 * frame) - np.cos(4 * frame))
    anim_object.set_data(xdata,ydata)
    
    return anim_object, 

#Пределы изменения переменной X и Y
ax.set_xlim(-20, 20)                                                                                   
ax.set_ylim(-20, 20)

animation_6_4_heart = anim.FuncAnimation(fig, heart_move, frames = np.linspace(0, 2*np.pi, 100), interval = 0.01)

animation_6_4_heart.save('animation_6_4_heart.gif')