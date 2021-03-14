print('Послание Аресибо')

#Подключение необходимых библиотек
import numpy as np
import matplotlib.pyplot as plt

import scipy.io.wavfile as wav
import scipy.signal as signal
from PIL import Image

#Первый файл
 
# Считываем файл
fs, data = wav.read('Arecibo.wav')
 
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    return b, a
 
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y
 
f1, f2 = 3000, 4000
data_f2 = butter_bandpass_filter(data, f2 - 200, f2 + 200, fs, order=3)

#Создание массива с обозначениями цветов
color = []

#Ввод переменной
n = 0
var = []
l=1102

#Перебор амплитуд и присвоение им соответствующего цвета в зависимости от величины
for i in range(0, 1679, 1):
     
    #Определение кол-ва амплитуд из массива data_f2 превышающих критическое значение амплитуды 
    var.append(sum(abs(data_f2[i*l:l*(i+1)]))/l)
          
#Определение кол-ва амплитуд, удовлетворяющих условию присуждения им белого цвета
for i in range(0, 1679, 1):           
    if var[i] > 700:
        color.append(2)
    elif var[i] <= 700:
        color.append(1)
    else:
        print('error')        

#Вспомогательные параметры функции             
fig, ax = plt.subplots(figsize=(23*0.2, 73*0.2), facecolor='pink')

#Создание белого фона
plt.plot(10,-10, marker='s', markersize=9999, color='white')

#Отрисовка точек
for i in range(0, 73, 1):    
    for k in range(0, 23, 1):
        if color[n+k]%2 == 1:        
            plt.plot(k, -i, 's', color='black', ms=11)
        elif color[n+k]%2 == 0:
            plt.plot(k, -i, 's', color='white', ms=11)
        else:
             print('error')
    n = n + 23

#Украшательства
plt.xlim(-0.5, 22.5)
plt.ylim(-72.5, 0.5)
plt.title('Первое послание (Arecibo.wav)')
plt.show()


#Второй файл

# Считываем файл
fs, data = wav.read('signal_1.wav')
 
f1, f2 = 3000, 4000
data_f2 = butter_bandpass_filter(data, f2 - 200, f2 + 200, fs, order=3)

#Создание массива с обозначениями цветов
color2 = []

#Ввод переменной
n2 = 0
var2 = []
l=1102

#Перебор амплитуд и присвоение им соответствующего цвета в зависимости от величины
for i in range(0, 1232, 1):

    #Определение кол-ва амплитуд из массива data_f2 превышающих критическое значение амплитуды    
    var2.append(sum(abs(data_f2[i*l:l*(i+1)]))/l)
    
    #Определение кол-ва амплитуд, удовлетворяющих условию присуждения им белого цвета
    if var2[i] > 700:
        color2.append(2)
    elif var2[i] <= 700:
        color2.append(1)
    else:
        print('error') 
    
#Вспомогательные параметры функции             
fig, ax = plt.subplots(figsize=(77*0.2, 16*0.2), facecolor='pink')

#Создание белого фона
plt.plot(10,-10, marker='s', markersize=9999, color='white')

#Отрисовка точек
for i in range(0, 16, 1):
    for k in range(0, 77, 1):
        if color2[n2+k]%2 == 1:        
            plt.plot(k, -i, 's', color='black', ms=11)
        elif color2[n2+k]%2 == 0:
            plt.plot(k, -i, 's', color='white', ms=11)
        else:
             print('error')
    n2 = n2 + 77
             
#Украшательства
plt.xlim(-0.5, 76.5)
plt.ylim(-15.5, 0.5)
plt.title('Второе послание (signal_1.wav)')
plt.show()


#Третий файл

# Считываем файл
fs, data = wav.read('signal_2.wav')
 
f1, f2 = 3000, 4000
data_f2 = butter_bandpass_filter(data, f2 - 200, f2 + 200, fs, order=3)

#Создание массива с обозначениями цветов
color = []

#Ввод переменной
n3 = 0
var3 = []
l=1102

#Перебор амплитуд и присвоение им соответствующего цвета в зависимости от величины
for i in range(0, 3000, 1): 
    
    #Определение кол-ва амплитуд из массива data_f2 превышающих критическое значение амплитуды       
    var3.append(sum(abs(data_f2[i*l:l*(i+1)]))/l)
                
    #Определение кол-ва амплитуд, удовлетворяющих условию присуждения им белого цвета                
    if var3[i] > 700:
        color.append(2)
    elif var3[i] <= 700:
        color.append(1)
    else:
        print('error') 

#Вспомогательные параметры функции             
fig, ax = plt.subplots(figsize=(92*0.2, 25*0.2), facecolor='pink')

#Создание белого фона
plt.plot(10,-10, marker='s', markersize=9999, color='white')

#Отрисовка точек
for i in range(0, 25, 1):
    for k in range(0, 92, 1):
        if color[n3+k]%2 == 1:        
            plt.plot(k, -i, 's', color='black', ms=11)
        elif color[n3+k]%2 == 0:
            plt.plot(k, -i, 's', color='white', ms=11)
        else:
             print('error')
    n3 = n3 + 92
             
#Украшательства
plt.xlim(-0.5, 91.5)
plt.ylim(-24.5, 0.5)
plt.title('Третье послание (signal_2.wav)')
plt.show()


#Четвертый файл

# Считываем файл
fs, data = wav.read('signal_3.wav')
 
f1, f2 = 3000, 4000
data_f2 = butter_bandpass_filter(data, f2 - 200, f2 + 200, fs, order=3)

#Создание массива с обозначениями цветов
color4 = []

#Ввод переменной
n4 = 0
var4 = []
l=1102

#Перебор амплитуд и присвоение им соответствующего цвета в зависимости от величины
for i in range(0, 1200, 1):  
    
    #Определение кол-ва амплитуд из массива data_f2 превышающих критическое значение амплитуды       
    var4.append(sum(abs(data_f2[i*l:l*(i+1)]))/l)               

    #Определение кол-ва амплитуд, удовлетворяющих условию присуждения им белого цвета
    if var4[i] > 700:
        color4.append(2)
    elif var4[i] <= 700:
        color4.append(1)
    else:
        print('error') 

#Вспомогательные параметры функции             
fig, ax = plt.subplots(figsize=(40*0.2, 30*0.2), facecolor='pink')

#Создание белого фона
plt.plot(10,-10, marker='s', markersize=9999, color='white')

#Отрисовка точек
for i in range(0, 30, 1):
    for k in range(0, 40, 1):
        if color4[n4+k]%2 == 1:        
            plt.plot(k, -i, 's', color='black', ms=11)
        elif color4[n4+k]%2 == 0:
            plt.plot(k, -i, 's', color='white', ms=11)
        else:
             print('error')
    n4 = n4 + 40
             
#Украшательства             
plt.xlim(-0.5, 39.5)
plt.ylim(-29.5, 0.5)
plt.title('Четвертое послание (signal_3.wav)')
plt.show()   