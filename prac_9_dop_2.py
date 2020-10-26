print('--------------------------------Dop_Zadanie_1-------------------------------')
print('Решение задачи про метеорит и что-то там')
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(1,100,1)
#g = np.arange(0.01,9.81,0.01)

def meteor(h,t):
    dgdt = -G * M / (r + h)**2
    dvdt = -dgdt * t
    return dvdt

G = 6.67 * 10**(-11)
M = 5.972 * 10**24
r = 6378140
h = 4 * 10**10 
v_0 = 0


solve_dif = odeint(meteor,v_0,t)

plt.plot(t,solve_dif[:,0])
plt.grid()
plt.show()
    