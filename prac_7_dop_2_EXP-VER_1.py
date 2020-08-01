print('-----------------------------Dop_Zadanie_2--------------------------------')
print('Экспериментальная версия, созданная от безысходности и тленности бытия. Функция создаёт анимацию вращения квадрата.')

#Подключение необходимых библиотек
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as anim   

#Создание пространства и подпространства для анимации 
fig, ax = plt.subplots(figsize=(10,10))              

#Создание анимируемого объкта
anim_object_1, = plt.plot([], [], color='r', label='Square')
anim_object_2, = plt.plot([], [], color='b', label='Square')
anim_object_3, = plt.plot([], [], color='g', label='Square')
anim_object_4, = plt.plot([], [], color='y', label='Square')

#Пределы изменения переменной x и y
ax.set_xlim(-25, 25)  
ax.set_ylim(-25, 25)
plt.grid()

#Функция создания и анимации квадрата

def square_move_1(l, angle_vel=None, time=None):
    """Функция делает анимацию вращающейгося квадрата.
       Внимание! Это экспериментальная версия функции, созданная от безысходности и тленности бытия
       На вход подаются:
       l - сторона квадрата
       angle_vel, time - необходимые для анимации параметры
    """    
    t = angle_vel * (np.pi / 180) * time  

    P = l #* np.sqrt(2)
    T = np.arange(P, 6 * P, P)    
    A1 = (1 // (T // P)) * (T // P)
    A2 = (2 // (T // P)) * ((T // P) // 2)
    A3 = (3 // (T // P)) * ((T // P) // 3)
    A4 = (4 // (T // P)) * ((T // P) // 4)
    A5 = T - P * (T // P)
    
    x = ((A2 + A3) * A5 + A4 * P) * np.cos(np.pi / 4) 
    y = ((A1 + A4) * A5 + A3 * P) * np.sin(np.pi / 4)
      
    X = x * np.cos(t) - y * np.sin(t)
    Y = y * np.cos(t) + x * np.sin(t)    
    return X, Y

def square_move_2(l, angle_vel=None, time=None):
    """Функция делает анимацию вращающейгося квадрата.
       Внимание! Это экспериментальная версия функции, созданная от безысходности и тленности бытия
       На вход подаются:
       l - сторона квадрата
       angle_vel, time - необходимые для анимации параметры
    """    
    t = angle_vel * (np.pi / 180) * time  

    P = l #* np.sqrt(2)
    T = np.arange(P, 6 * P, P)    
    A1 = (1 // (T // P)) * (T // P)
    A2 = (2 // (T // P)) * ((T // P) // 2)
    A3 = (3 // (T // P)) * ((T // P) // 3)
    A4 = (4 // (T // P)) * ((T // P) // 4)
    A5 = T - P * (T // P)
    
    x = ((A2 + A3) * A5 + A4 * P) * np.cos(7 * np.pi / 4)
    y = ((A1 + A4) * A5 + A3 * P) * np.sin(7 * np.pi / 4)
      
    X = x * np.cos(t) - y * np.sin(t)
    Y = y * np.cos(t) + x * np.sin(t)    
    return X, Y

def square_move_3(l, angle_vel=None, time=None):
    """Функция делает анимацию вращающейгося квадрата.
       Внимание! Это экспериментальная версия функции, созданная от безысходности и тленности бытия
       На вход подаются:
       l - сторона квадрата
       angle_vel, time - необходимые для анимации параметры
    """    
    t = angle_vel * (np.pi / 180) * time  

    P = l #* np.sqrt(2)
    T = np.arange(P, 6 * P, P)    
    A1 = (1 // (T // P)) * (T // P)
    A2 = (2 // (T // P)) * ((T // P) // 2)
    A3 = (3 // (T // P)) * ((T // P) // 3)
    A4 = (4 // (T // P)) * ((T // P) // 4)
    A5 = T - P * (T // P)
    
    x = ((A2 + A3) * A5 + A4 * P) * np.cos(13 * np.pi / 4) 
    y = ((A1 + A4) * A5 + A3 * P) * np.sin(13 * np.pi / 4)
      
    X = x * np.cos(t) - y * np.sin(t)
    Y = y * np.cos(t) + x * np.sin(t)    
    return X, Y

def square_move_4(l, angle_vel=None, time=None):
    """Функция делает анимацию вращающейгося квадрата.
       Внимание! Это экспериментальная версия функции, созданная от безысходности и тленности бытия
       На вход подаются:
       l - сторона квадрата
       angle_vel, time - необходимые для анимации параметры
    """    
    t = angle_vel * (np.pi / 180) * time  

    P = l #* np.sqrt(2)
    T = np.arange(P, 6 * P, P)    
    A1 = (1 // (T // P)) * (T // P)
    A2 = (2 // (T // P)) * ((T // P) // 2)
    A3 = (3 // (T // P)) * ((T // P) // 3)
    A4 = (4 // (T // P)) * ((T // P) // 4)
    A5 = T - P * (T // P)
    
    x = ((A2 + A3) * A5 + A4 * P) * np.cos(19 * np.pi / 4) 
    y = ((A1 + A4) * A5 + A3 * P) * np.sin(19 * np.pi / 4)
      
    X = x * np.cos(t) - y * np.sin(t)
    Y = y * np.cos(t) + x * np.sin(t)    
    return X, Y

#Функция анимации
def animate(i):
    anim_object_1.set_data(square_move_1(l = 20, angle_vel = 1, time = i))
    anim_object_2.set_data(square_move_2(l = 20, angle_vel = 1, time = i))
    anim_object_3.set_data(square_move_3(l = 20, angle_vel = 1, time = i))
    anim_object_4.set_data(square_move_4(l = 20, angle_vel = 1, time = i))
    ax.set_title('time, day{}'.format(i))
    
#Создание анимации
animation_7_dop_2 = anim.FuncAnimation(fig,animate,frames=300,interval=0.1)

#Сохранение анимации
animation_7_dop_2.save('animation_7_dop_2.gif')
