print('-----------------------------Zadanie_3--------------------------------')
print('Функция, cоздающая анимацию двух бегущих синусоид вида y(t) = A*sin(f*t) c разными A и f.')

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as anim  
                
#Создание пространства и подпространства для анимации
fig, ax = plt.subplots()                                                                                      

#Создание первого и второго анимируемых объктов
anim_object_1, = plt.plot([], [], marker='o', color='red', ms=5, label='Sinusoida_1')                      
anim_object_2, = plt.plot([], [], marker='o', color='orange', ms=5, label='Sinusoida_2') 

#Координаты анимируемого объекта
xdata_1, ydata_1 = [], []
xdata_2, ydata_2 = [], []                  

def sinusoida_move(frame=None, A_1 = 5, f_1 = 5, A_2 = 8, f_2 = 3):
    """Функция cоздаёт анимацию двух бегущих синусоид вида y(t) = A*sin(f*t) c разными A и f.
       На вход подаются:
       frame - кол-во кадров в секунду
       A - высота амплитуды
       f - частота
    """
    t = np.linspace(0, frame, 500)
    
    xdata_1.append(t)
    ydata_1.append(A_1 * np.sin(f_1 * t))
    anim_object_1.set_data(xdata_1, ydata_1)
    
    xdata_2.append(t)
    ydata_2.append(A_2 * np.sin(f_2 * t))
    anim_object_2.set_data(xdata_2, ydata_2)
    
    return anim_object_1, anim_object_2, 

#Пределы изменения переменной X и Y
ax.set_xlim(0,  2 * np.pi)
ax.set_ylim(-8, 8)

animation_6_3 = anim.FuncAnimation(fig, sinusoida_move, frames = np.linspace(0, 2 * np.pi, 100), interval=0.001)

animation_6_3.save('animation_6_3.gif')