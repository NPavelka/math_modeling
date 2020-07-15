print('-----------------------------Dop_Zadanie_2--------------------------------')
print('Эллипс через полярные координаты')

import matplotlib.pyplot as plt 
import numpy as np

def ellipse_pol(p = 2, e = 0.5, title='Crivai-ellipse'):
    """Функция строит эллипс через полярные координаты. На вход подаются:
       p - фокальный параметр
       e - эксцентриситет (от 0 до 1)
       title - название кривой
    """
    f = np.arange(0, 8* np.pi, 0.01)
        
    if e >= 1 or e <= 0:
        print('Задан не правильный эксцентриситет: ', e)

    r = p / (1 + e * np.cos(f))
    
    x = r * np.cos(f)
    y = r * np.sin(f)
    
    plt.plot(x, y, label='Ellipse', color='purple')
    
    plt.grid()
    plt.title('Ellipse')                            
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')
    plt.axis('equal')  

    plt.show()
    
ellipse_pol(6, 0.8)   