print('-----------------------------Zadanie_3--------------------------------')

import numpy as np
from scipy.constants import g

def brosok(x_0, y_0, V_0, a, t = None):
    
    a = a * np.pi / 180
    x = x_0
    y = y_0
    t = 0
    
    Z = np.ndarray(shape = (500,3))
    
    for i in np.arange(0, 500, 1):
        
        t = t + 0.01
        
        x = x_0 + V_0 * t * np.cos(a)
        y = y_0 + V_0 * t * np.sin(a) - (g * t**2) / 2  
        
        Z[i, 0] = t
        Z[i, 1] = x
        Z[i, 2] = y
        
    print(Z)

    return Z

x_0 = int(input('Введите начальную координату x_0:'))
y_0 = int(input('Введите начальную координату y_0:'))
V_0 = int(input('Введите начальную скорость V_0:'))
a = int(input('Введите угол броска по отношению к горизонту(в градусах):'))

brosok(x_0, y_0, V_0, a)




































