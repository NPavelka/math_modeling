print('Объект в гравитационном поле чёрной дыры')

#Подключение необходимых для программы библиотек
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from scipy.integrate import odeint

# Константы
G = 6.67*10**(-11)                              #Гравитационная постоянная
Ms = 1.989*10**30                               #Масса Солнца, кг
M = Ms*5*10**6                                  #Масса черной дыры, кг
c = 3*10**8                                     #Скорость света, м/с

# Начальные параметры
a = 20*1.496*10**11                             #Большая полуось, м
e = 0.8                                         #Эксцентриситет

# Данные постоянные
p = a * (1 - e**2)                              #Фокальный параметр, м
l = np.sqrt(p*G*M)                              #Момент импульса на единицу массы
rg = 2*G*M / c**2                               #Гравитационный радиус черной дыры, м
Q = a*(1 + e)                                   #Апоцентр, м
q = a*(1 - e)                                   #Перицентр, м
T = np.sqrt((4 * np.pi**2 * a**3) / (G * M))    #Сидерический период, с

Vc = np.sqrt(G*M/a)                             #Круговая скорость
V_Q = Vc*np.sqrt((1-e)/(1+e))                   #Cкорость в апоцентре

#Начальные изменяемые параметры объектов
#Планета
x_0 = Q
Vx_0 = 0

y_0 = 0
Vy_0 = -V_Q

phi_0 = 0

#Черная дыра
xh0 = 0
Vxh0 = 0
yh0 = 0
Vyh0 = 0

#Прочее (тоже планета)
r_0 = Q
Vr_0 = 0

#определяем пределы переменной величины (времени)
t = np.arange(0, 85*T, 6*3600)   # 1 кадр = 6 часов => примерно 5000 кадров всего для 85 периодов (4969)

#Определение функции для системы диф. уравнений
def func(Z,t):
    (x, Vx, y, Vy, phi, xh, Vxh, yh, Vyh, r, Vr) = Z
    
    dxdt = Vx + Vr*np.cos(phi)
    dVxdt = -G*M*(x-xh)/((x-xh)**2+(y-yh)**2)**1.5

    dydt = Vy + Vr*np.sin(phi)
    dVydt = -G*M*(y-yh)/((x-xh)**2+(y-yh)**2)**1.5
    
    dphidt = 1 / (dxdt**2 + dydt**2)

    dxhdt = 0
    dVxhdt = 0
    dyhdt = 0
    dVyhdt = 0
    
    drdt = (dxdt**2 + dydt**2)**0.5
    dVrdt = -(rg * c**2) / (2 * r**2) + l**2 / r**3 - 3 * (l**2 * rg) / r**4    
        
    return dxdt, dVxdt, dydt, dVydt, dphidt, dxhdt, dVxhdt, dyhdt, dVyhdt, drdt, dVrdt

Z_0 = (x_0, Vx_0, y_0, Vy_0, phi_0, xh0, Vxh0, yh0, Vyh0, r_0, Vr_0)

solve_sys = odeint(func,Z_0,t)

#print(solve_sys)

# Модуль анимации
fig,ax = plt.subplots(figsize=(10,10), facecolor='lightgrey')

# Создание маркеров планет и объектов
Obj_1,=plt.plot([],[],marker='.',markersize=10, color='green')
Obj_2,=plt.plot([],[],marker='o',markersize=10, color='black')

#Создание функции анимации
def animate(i):
    Obj_1.set_data(solve_sys[i,0],solve_sys[i,2])
    Obj_2.set_data(solve_sys[i,5],solve_sys[i,7])
    
    #Определение временного периода
    ax.set_title('time, quarter days {}'.format(i))

animation = anim.FuncAnimation(fig,animate,frames=4969,interval=30)

#Украшательства
plt.grid()
plt.xlim(-3*a,3*a)
plt.ylim(-3*a,3*a)

#Итог
animation.save('Black hole.gif') #Открывать в хроме, не в эксплоере