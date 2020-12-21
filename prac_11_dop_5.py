print('--------------------------------Dop_Zadanie_5-------------------------------')
print('Решение задачи про температуры на этажах')

#Подключение необходимых для программы библиотек
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#определяем пределы переменной величины (времени)
t = np.arange(0, 30, 0.1)

#Константы 
alpha_1 = 0.1     #Пол и 1 этаж
alpha_2 = 0.2     #Стены 
alpha_3 = 0.5     #Потолок между 1 и 2

#T = 273 #K

Tg = 10 #+ T      #Температура земли
Te = 8 #+ T       #Температура воздуха вне дома
Tw = 5            #Температура источника

#Начальные изменяемые параметры объектов
T1_0 = 17 #+ T
T2_0 = 9 #+ T

Z_0 = T1_0, T2_0

print('---------------------Случай без источника---------------------')

def func_1(Z,t):
    T1, T2 = Z
    
    dT1dt = alpha_1*(Tg - T1) + alpha_2*(Te - T1) + alpha_3*(T2 - T1)
    dT2dt = alpha_2*(Te - T2) + alpha_3*(T1 - T2)
    
    return dT1dt, dT2dt

sys1 = odeint(func_1,Z_0,t)

plt.plot(t,sys1[:,0], label = 'T1 без источника')
plt.plot(t,sys1[:,1], label = 'T2 без источника')

plt.legend()
plt.grid()
plt.xlabel('Время')
plt.ylabel('Температера, *С')
plt.show()

print('---------------------Случай с источником---------------------')

def func_2(Z,t):
    T1, T2 = Z
    
    dT1dt = alpha_1*(Tg - T1) + alpha_2*(Te - T1) + alpha_3*(T2 - T1) + Tw
    dT2dt = alpha_2*(Te - T2) + alpha_3*(T1 - T2)
    
    return dT1dt, dT2dt

sys2 = odeint(func_2,Z_0,t)

plt.plot(t,sys2[:,0], label = 'T1 с источником')
plt.plot(t,sys2[:,1], label = 'T2 с источником')

plt.legend()
plt.grid()
plt.xlabel('Время')
plt.ylabel('Температера, *С')
plt.show()