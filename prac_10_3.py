print('--------------------------------Zadanie_3-------------------------------')
print('Решение закона всемирного тяготения')

#Подключение необходимых для программы библиотек
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as anim

#Определение переменной величины уравнений
t = np.arange(0, 10*365*24*3600, 36000)

#Определение функции для системы диф. уравнений
def G_func(Z, t):
    x, Vx, y, Vy = Z
    
    dxdt = Vx
    dVxdt = - (G * M * x) / (x**2 + y**2)**1.5
    
    dydt = Vy
    dVydt = - (G * M * y) / (x**2 + y**2)**1.5
    
    return dxdt, dVxdt, dydt, dVydt

#Определение начальных условий и параметры, входящие в систему диф. уравнений
x_0 = 0
Vx_0 = -29783
y_0 = 1.496 * 10**11
Vy_0 = 0

M = 1.9885 * 10**30
G = 6.67 * 10**(-11)

Z_0 = x_0, Vx_0, y_0, Vy_0

#Решаем систему диф. уравнений
sol = odeint(G_func, Z_0, t)

# Модуль анимации
fig,ax = plt.subplots()

#Строим решение в виде графика
#plt.plot(sol[:, 0], sol[:, 2], 'b', label='Earth')
Obj_1,=plt.plot([], [],marker='.',markersize=10, color='brown')
Sun,=plt.plot(0, 0, marker='.', ms=25, color='orange')

def animate(i):
    Obj_1.set_data(sol[i,0],sol[i,2])
    ax.set_title('time'.format(i))
#Строим 

sun_animation = anim.FuncAnimation(fig,animate,frames=200,interval=30)

plt.axis('equal')
plt.legend()
plt.grid()
plt.xlim(-2*1.496 * 10**11,2*1.496 * 10**11)
plt.ylim(-2*1.496 * 10**11,2*1.496 * 10**11)
plt.show()
sun_animation.save('Movement.gif')
