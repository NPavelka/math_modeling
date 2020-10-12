print('--------------------------------Zadanie_2-------------------------------')
print('Решение задачи про инвистиции в предприятие')

#Подключение необходимых для программы библиотек
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#import matplotlib.animation as anim

#Пределы изменения переменной величины
t = np.linspace(0,1460,365)  #дни

def Inf_func(I,t):
    dIdt = - I * k
    return dIdt

#Определение начальных условий и параметров
I_0 = 1000                   #единиц
k_p = 0.08                   #коофициент

#Решение дифференциального уравнения функцией odeint
k = k_p
solve_i = odeint(Inf_func, I_0, t)

#Построение решения в виде графика функции
plt.plot(t, solve_i[:,0], color='orange', label='Количество инвистиций')

plt.legend()
plt.grid()
plt.show()