print('-----------------------------Zadanie_3/1--------------------------------')
print('Функция, строящая графики кривых, заданных параметрически: Циклоиды и Астроиды, а также анимирует движение точки по ним.')

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as anim                  

#Создание пространства и подпространства для анимации 
fig, ax = plt.subplots(figsize=(12,6))              

#Создание анимируемого объкта
anim_object, = plt.plot([], [],color='orange', label='Cicloida')

def cicloida_move(R=1, r=2, angle_vel=None, time=None):
    """Функция строит циклоиду: кривая, описанная точкой, лежащей на окружности радиуса R, если эта окружность катится без скольжения по прямой.
       На вход подаются:
       R - радиус циклоиды
       r - радиус окружности
       angle_vel, time - необходимые для анимации параметры
    """
    t = angle_vel * (np.pi / 180) * time
    alpha = np.linspace(0, 2 * np.pi, 30)
    
    x0 = R * (t - np.sin(t)) 
    y0 = R * (1 - np.cos(t)) 
    
    x = x0 + r * np.cos(alpha)
    y = y0 + r * np.sin(alpha)
    return x, y

def cicloida(R, angle_vel=None, time=None):
    t = angle_vel * (np.pi / 180) * time
    x0 = R * (t - np.sin(t)) 
    y0 = R * (1 - np.cos(t))
    return x0, y0

#Пределы изменения переменной X и Y
ax.set_xlim(-1, 20)  
ax.set_ylim(-3, 6)

def animate(i):
    anim_object.set_data(cicloida_move(R = 1, r = 0.5, angle_vel = 1, time = i))
    ax.set_title('time, frame{}'.format(i))

animation_7_3 = anim.FuncAnimation(fig, animate, frames=200, interval=1)

sub = cicloida(R = 1, angle_vel = 360, time = np.arange(0, 2 * np.pi, 0.01))
plt.plot(sub[0],sub[1], color = 'g')

animation_7_3.save('animation_7_3_cic.gif')