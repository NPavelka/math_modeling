print('--------------------------------Zadanie_2-------------------------------')
print('Решение уравнения Чебушева')

#Подключение необходимых для программы библиотек
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Определение переменной величины уравнений
x = np.arange(-0.99, 0.99, 0.001)

#Определение функции для системы диф. уравнений
def Cheb_func(Z, x):
    y, omega = Z
    dy_dt = omega
    domega_dt = (x * omega - n**2 * y) / (1 - x**2)
    return dy_dt, domega_dt

#Определение начальных условий и параметры, входящие в систему диф. уравнений
y_0 = 4
omega_0 = 20
n = 0.1
Z_0 = y_0, omega_0

#Решаем систему диф. уравнений
sol = odeint(Cheb_func, Z_0, x)

#Строим решение в виде графика
plt.plot(x, sol[:, 0], 'g', label='y(x)')
plt.legend()
plt.grid()
plt.show()