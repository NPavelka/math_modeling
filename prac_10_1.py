print('--------------------------------Zadanie_1-------------------------------')
print('Решение уравнения Бесселя')
#Подключение необходимых для программы библиотек
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Определение переменной величины уравнений
x = np.arange(0.01, 1, 0.0001)

#Определение функции для системы диф. уравнений
def Bess_func(Z, x):
    y, omega = Z
    dy_dt = omega
    domega_dt = (y * (x**2 - V**2) - x * omega) / x**2
    return dy_dt, domega_dt

#Определение начальных условий и параметры, входящие в систему диф. уравнений
y_0 = 0.5
omega_0 = 3
V = 1/3
Z_0 = y_0, omega_0

#Решаем систему диф. уравнений
sol = odeint(Bess_func, Z_0, x)

#Строим решение в виде графика
plt.plot(x, sol[:, 0], 'g', label='y(x)')
plt.legend()
plt.grid()
plt.show()