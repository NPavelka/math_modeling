print('Диаграмма Герцшпрунга — Рассела')

#Подключение необходимых библиотек
import numpy as np
import matplotlib.pyplot as plt

#Импорт данных из текстовых файлов
filename_B_V = 'data_B_V.txt'
filename_B_V_1 = 'data_B_V_1.txt'
filename_M = 'data_M.txt'
filename_M_1 = 'data_M_1.txt'

#Распаковка данных в списки
data_BV = np.loadtxt(filename_B_V, dtype=float)
data_BV1 = np.loadtxt(filename_B_V_1, dtype=float)
data_M = np.loadtxt(filename_M, dtype=float)
data_M1 = np.loadtxt(filename_M_1, dtype=float)

#Перевод показателя цвета B-V в температуру
B_V = data_BV
T_1 = 4600 * (1/(0.92 * B_V + 1.7) + 1/(0.92 * B_V + 0.62))

B_V_1 = data_BV1
T_2 = 4600 * (1/(0.92 * B_V_1 + 1.7) + 1/(0.92 * B_V_1 + 0.62))

M_1 = data_M

M_2 = data_M1

#Создание программы отрисовки точек
def diagramm(T_1, T_2, M_1, M_2):
    
    #Подключение программы перевода температуры в цвет RGB
    def kelvin_to_color(Kel=10000):
        ''' Функция возвращающая цвет (в RGB форме) звезды, по температуре
            поверхности, подающейся на вход функции.
        '''    
        Kel = Kel / 100
        # Вычисление красного
        if Kel <= 66:
            Red = 255
        else:
            Red = Kel - 60
            Red = 329.698727446*Red**(-0.1332047592)
            if Red < 0:
                Red = 0
            if Red > 255 :
                Red = 255
        r = Red / 255
    
        # Вычисление зелёного
        if Kel <= 66:
            Green = Kel
            Green = 99.4708025861 * np.log(Green) - 161.1195681661
            if Green < 0:
                Green = 0
            if Green > 255:
                Green = 255
        else:
            Green = Kel - 60
            Green = 288.1221695283 * Green**(-0.0755148492)
            if Green < 0:
                Green = 0
            if Green > 255:
                Green = 255
        g = Green / 255
    
        # Вычисление синего
        if Kel >= 66:
            Blue = 255
        else:
            if Kel <= 19:
                Blue = 0
            else:
                Blue = Kel - 10
                Blue = 138.5177312231 * np.log(Blue) - 305.0447927307
                if Blue < 0:
                    Blue = 0
                if Blue > 255:
                    Blue = 255
        b = Blue / 255
    
        return (r, g, b)
    
    #количество точек в каждом из списков
    n_1 = 86492
    n_2 = 117731
    
    #Создание списков цвета
    temp_1 = []
    temp_2 = []
    
    #Перевод температуры в показатели цвета RGB
    for i in range(0, n_1, 1):        
        t1 = kelvin_to_color(T_1[i])
        temp_1.append(t1)
        print('Процесс обработки данных (1/2) завершен на ',i,' из 86492 пунктов. Ожидайте. Это будет оооочень долго подгружаться...')
        
    for i in range(0, n_2, 1):        
        t2 = kelvin_to_color(T_2[i])
        temp_2.append(t2)
        print('Процесс обработки данных (2/2) завершен на ',i,' из 117731 пунктов. Ожидайте. Лучше пойдите и сделайте себе чай... или кофе.')          
    
    #Вспомогательные параметры функции
    fig, ax = plt.subplots(figsize=(10,10), facecolor='pink')
    
    #Задание координат
    x_1 = -T_1
    y_1 = -M_1
    
    x_2 = -T_2
    y_2 = -M_2
    
    #Отрисовка черного фона (да, через одну большую черную точку, а что?)
    plt.plot(-10000,-5, marker='o', markersize=2000, color='black')
    
    #Отрисовка всех точек из первого и второго списка
    for i in range(0, n_1, 1):
        plt.plot(x_1[i],y_1[i], color = temp_1[i], marker='.', markersize=0.5)
        print('Процесс отрисовки точек (1/2) завершен на ',i,' из 86492 пунктов. Ожидайте. Я серьезно. Сделайте себе чай, возьмите печеньки...наслаждайтесь...')
        
    for i in range(0, n_2, 1):
        plt.plot(x_2[i],y_2[i], color = temp_2[i], marker='.', markersize=0.5)
        print('Процесс отрисовки точек (2/2) завершен на ',i,' из 117731 пунктов. Ожидайте. Надеюсь, ваш чай еще не остыл. Скоро вы увидете итог...')
    
    print('Диаграмма Герцшпрунга — Рассела')
    
    #Итог всей программы    
    plt.show()
    
#Итог   
diagramm(T_1, T_2, M_1, M_2)
print('В значениях необходимо поменять знак с (-) на (+)')
    