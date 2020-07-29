print('-----------------------------Zadanie_4/1--------------------------------')
print('Функция рисует бабочку.')

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as anim                  

#Создание пространства и подпространства для анимации 
fig, ax = plt.subplots()                                                                               

#Создание анимируемого объкта
anim_object, = plt.plot([], [], marker='o', color='orange', ms=10, label='Butterfly')                  

#Координаты анимируемого объекта
xdata, ydata = [], []                                          

def butterfly_move(frame=None):
    """Функция рисует бабочку.
       На вход подаются:
       frame - количество кадров в секунду
    """
    xdata.append(np.sin(frame) * (np.e**(np.cos(frame)) - 2 * np.cos(4 * frame) + np.sin(frame / 12)**5))
    ydata.append(np.cos(frame) * (np.e**(np.cos(frame)) - 2 * np.cos(4 * frame) + np.sin(frame / 12)**5))
    anim_object.set_data(xdata,ydata)
    
    return anim_object, 

#Пределы изменения переменной X и Y
ax.set_xlim(-5, 5)                                                                                   
ax.set_ylim(-5, 5)

animation_6_4_but = anim.FuncAnimation(fig, butterfly_move, frames = np.linspace(0, 12*np.pi, 1000), interval = 0.01)

animation_6_4_but.save('animation_6_4_but.gif')