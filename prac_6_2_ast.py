print('-----------------------------Zadanie_2/2--------------------------------')
print('Функция, строящая графики кривых, заданных параметрически: Циклоиды и Астроиды, а также анимирует движение точки по ним.')

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as anim                  

fig, ax = plt.subplots()                                                                            #Создание пространства и подпространства для анимации  

anim_object, = plt.plot([], [], marker='o', color='red', ms=10, label='Аstroida')                   #Создание анимируемого объкта

def astroida_move(R=1, angle_vel=None, time=None):
    """Функция строит астроиду: кривая, описанная точкой, лежащей на окружности радиуса R, если эта окружность катится без скольжения по прямой.
       На вход подаются:
       R - радиус окружности
       angle_vel, time - необходимые для анимации параметры
    """
    t = angle_vel * (np.pi / 180) * time
    
    x = R * np.cos(t)**3
    y = R * np.sin(t)**3
    
    return x, y  

ax.set_xlim(-10, 10)                                                                                #Пределы изменения переменной X
ax.set_ylim(-10, 10)                                                                                #Пределы изменения переменной Y

def animate(i):
    anim_object.set_data(astroida_move(R = 5, angle_vel = 1, time=i))
    ax.set_title('time, day{}'.format(i))

animation_6_2 = anim.FuncAnimation(fig,
                                   animate,
                                   frames=1000,
                                   interval=0.1)

sub = astroida_move(R = 5, angle_vel = 1080,time = np.arange(0, 2 * np.pi, 0.01))
plt.plot(sub[0],sub[1], color = 'b')
animation_6_2.save('animation_6_2_ast.gif')