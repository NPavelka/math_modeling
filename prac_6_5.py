print('-----------------------------Zadanie_5--------------------------------')
print('Функция координаты n-ой точки фрактального множества.')

import matplotlib.pyplot as plt 
import matplotlib.animation as anim 

#Создание пространства и подпространства для анимации 
fig, ax = plt.subplots()                                                                               

#Создание анимируемого объкта
anim_object, = plt.plot([], [], marker='o', color='purple', ms=5, label='Heart')                  

#Координаты анимируемого объекта
xdata, ydata = [], []

def fractal_move(n = 50, C = 0.3, D = 0.33):
    """Функция рисует фрактал.
       На вход подаются:
       n - кол-во точек
       С и D - какие-то параметры
    """
    if n == 0:
        xdata.append(0.1)
        ydata.append(0.1)
    else:    
        xdata.append(xdata[n-1]**2 - ydata[n-1]**2 + C)
        ydata.append(2 * xdata[n-1] * ydata[n-1] + D)
    anim_object.set_data(xdata,ydata)
    
    return anim_object, 

#Пределы изменения переменной X и Y
ax.set_xlim(-0.2, 0.5)                                                                                   
ax.set_ylim(0, 0.7)

animation_6_5 = anim.FuncAnimation(fig, fractal_move, frames = 500, interval = 0.01)

animation_6_5.save('animation_6_5.gif')