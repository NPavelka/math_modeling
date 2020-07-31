print('-----------------------------Zadanie_4--------------------------------')
print('Функция, строящая графики кривых, заданных параметрически: Циклоиды и Астроиды, а также анимирует движение точки по ним.')

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as anim    

#Создание пространства и подпространства для анимации 
fig, ax = plt.subplots(figsize=(8,8))              

#Создание анимируемого объкта
anim_object, = plt.plot([], [], color='red', label='Аstroida')

def astroida_move(R=1, r=2, angle_vel=None, time=None):
    """Функция строит астроиду: кривая, описанная точкой, лежащей на окружности радиуса R, если эта окружность катится без скольжения по прямой.
       На вход подаются:
       R - радиус окружности
       angle_vel, time - необходимые для анимации параметры
    """
    t = angle_vel * (np.pi / 180) * time
    alpha = np.linspace(0, 2 * np.pi, 30)
    
    x0 = R * np.cos(t)**3
    y0 = R * np.sin(t)**3
    
    x = x0 + r * np.cos(alpha)
    y = y0 + r * np.sin(alpha)
    
    return x, y  

def astroida(R=1, angle_vel=None, time=None):
    t = angle_vel * (np.pi / 180) * time
    x = R * np.cos(t)**3
    y = R * np.sin(t)**3
    return x, y  

ax.set_xlim(-10, 10)                                                                                #Пределы изменения переменной X
ax.set_ylim(-10, 10)                                                                                #Пределы изменения переменной Y

def animate(i):
    anim_object.set_data(astroida_move(R = 5, r = 0.5, angle_vel = 1, time=i))
    ax.set_title('time, day{}'.format(i))

animation_7_4 = anim.FuncAnimation(fig, animate,frames=400,interval=0.1)

sub = astroida(R = 5, angle_vel = 1080,time = np.arange(0, 2 * np.pi, 0.01))
plt.plot(sub[0],sub[1], color = 'b')

animation_7_4.save('animation_7_4_ast.gif')