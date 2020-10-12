print('--------------------------------Zadanie_3-------------------------------')
print('Решение задачи про сопротивление среды')

#Подключение необходимых для программы библиотек
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#import matplotlib.animation as anim

#Пределы изменения переменной величины
t = np.linspace(0, 30, 100)  #секунды

def sopr_func(V,t):
    dVdt = F / m + (y * V**2) / m
    return dVdt

#Определение начальных условий и параметров
F = 8                      #сила, H
m = 15                     #масса, кг
y_0 = 0.06                 #коэффициент
V_0 = 0                    #Начальная скорость

#Решение дифференциального уравнения функцией odeint
y = y_0
solve_i = odeint(sopr_func, V_0, t)

#Построение решения в виде графика функции
plt.plot(t, solve_i[:,0], color='c', label='Изменение скорости')

plt.xlabel('Время, t, с')
plt.ylabel('Скорость, V, м/с')
plt.legend()
plt.grid()
plt.show()