print('--------------------------------Zadanie_1-------------------------------')
print('Решение задачи про размножения бактерий')

#Подключение необходимых для программы библиотек
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#import matplotlib.animation as anim

#Пределы изменения переменной величины
t = np.linspace(0,2,1000)  #секунды

def bac_func(m,t):
    dmdt = k*m
    return dmdt

#Определение начальных условий и параметров
m_0 = 1                     #кг
k_razmnozh = 2                 #1/с

#Решение дифференциального уравнения функцией odeint
k = k_razmnozh
solve_raz = odeint(bac_func, m_0, t)

#Построение решения в виде графика функции
plt.plot(t, solve_raz[:,0], color='green', label='Размножение Бактерий')

plt.legend()
plt.grid()
plt.show()