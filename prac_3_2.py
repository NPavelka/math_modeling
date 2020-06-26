print('-----------------------------Zadanie_2/1--------------------------------')

import numpy as np
from scipy.constants import g

h = 100
a = np.pi / 3
b = np.pi / 6

V = ((g * h * np.tan(b)**2) / (2 * np.cos(a)**2 * (1 - np.tan(b) * np.tan(a))))**0.5

print('V =',V)

print('-----------------------------Zadanie_2/2--------------------------------')

import numpy as np
from scipy.constants import e, h, k

T = 200
E = 300

N = (2 / np.pi**0.5) * (h / (k*T)**1.5) * e**(-E / (k*T)) * E**(T/2)

print('N =',N)