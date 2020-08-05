print('-----------------------------Dop_Zadanie_2--------------------------------')
print('Функция создаёт анимацию вращения квадрата, который на самом деле не квадрат, а всего лишь круг, состоящий из четырёх точек.')

#Подключение необходимых библиотек
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as anim   

#Создание пространства и подпространства для анимации 
fig, ax = plt.subplots(figsize=(10,10))              

#Создание анимируемого объкта
anim_object, = plt.plot([], [], color='r', label='Square')

#Пределы изменения переменной x и y
ax.set_xlim(-20, 20)  
ax.set_ylim(-20, 20)
plt.grid()

#Функция создания и анимации квадрата
def square_move(l, angle_vel=None, time=None):
    """Функция делает анимацию вращающейгося квадрата.
       На вход подаются:
       l - сторона квадрата
       angle_vel, time - необходимые для анимации параметры
    """    
    t = angle_vel * (np.pi / 180) * time
    alpha = np.linspace(0, 2 * np.pi, 5)
    
    r = l / 2**0.5
    
    x = r * np.cos(alpha)
    y = r * np.sin(alpha)
    
    X = x * np.cos(t) - y * np.sin(t)
    Y = y * np.cos(t) + x * np.sin(t)
        
    return X, Y

#Функция анимации
def animate(i):
    anim_object.set_data(square_move(l = 20, angle_vel = 1, time = i))
    ax.set_title('time, day{}'.format(i))
    
#Создание анимации
animation_7_dop_2 = anim.FuncAnimation(fig,animate,frames=100,interval=0.1)

#Сохранение анимации
animation_7_dop_2.save('animation_7_dop_2.gif')