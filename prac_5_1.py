print('-----------------------------Zadanie_1--------------------------------')
print('Построение квадрата с соответствующими координатами')

import matplotlib.pyplot as plt

x = [1,1,5,5,1]
y = [1,5,5,1,1]

plt.plot(x,y,color='k')

plt.xlim(-1,7)
plt.ylim(-1,7)

plt.plot([1], [1],marker='.', markersize=30, color='k')
plt.plot([1], [5],marker='.', markersize=30, color='k')
plt.plot([5], [5],marker='.', markersize=30, color='k')
plt.plot([5], [1],marker='.', markersize=30, color='k')

x = [6,0,0]
y = [0,0,6]

plt.plot(x,y,color='k')

plt.plot([0], [6],marker='^', markersize=10, color='k')
plt.plot([6], [0],marker='>', markersize=10, color='k')

plt.show()