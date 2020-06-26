#--------------------------Модули и библиотеки---------------------------------
#--------------------------Работа с модулями--------------------------------------------
#--------------------------Инструкция import-----------------------------------

import my_module               #Импорт модуля

print(my_module.a)             #Вызов параметра из модуля

A = my_module.a**2             #Использование модуля

print(A)

#--------------------------Инструкция import-as--------------------------------

import my_module as mm         #Импорт модуля с новым наименованием

print(mm.a)                    #Вызов параметра из модуля

A = mm.a**2                    #Использование модуля

print(A)

print(mm.a/(1 - mm.a**3))

#--------------------------Инструкция from-------------------------------------

from my_module import a        #Инструкция, копирующая атрибуты модуля

print(a)

#--------------------------Инструкция from *------------------------------------

from my_module import a, b, c  #Можно так

print(a, b, c)

from my_module import *        #Инструкция, копирующая все атрибуты модуля

print(a * b - c)

#--------------------------Инструкция from-import-as---------------------------

from astro_constans import earth_mass as em
import astro_constans as ac

print(em * 10)

#-------------------------------Библиотеки----------------------------------------------
#-----------------------------Библиотека math----------------------------------

from math import sin, tan, sqrt, pi

sin(2*pi)
sin(pi)

print(sqrt(3**2 - 5 * sin(pi / 2)))

#-----------------------------Библиотека numpy------------------------------------------

import numpy as np

#-----------------------------np.array-----------------------------------------
a = [1, 2, 4]

b = np.array(a)             #Создание массива из списка

print(type(a))    #<class 'list'>
print(type(b))    #<class 'numpy.ndarray'>

print(b * b)      #[ 1  4 16]
print(b / b)      #[1. 1. 1.]
print(b - b)      #[0 0 0]

#------------------np.zeros, np.ones и np.ndarray------------------------------

A = np.zeros((2,3))         #Создание таблицы с нулями
print(A)

A[0, 2] = 5                 #Включение в таблицу параметров

B = np.ones((3,2))          #Создание таблицы с единицами
print(B)

C = np.ndarray(shape = (2,3)) #Храненеие неких элементов

#-----------------------------np.arange----------------------------------------

for i in np.arange(0, 1, 0.1):
    print(i, end = ' ')

#-----------------------len - длина списка (кол-во элементов/строк)------------

a = np.arange(0, 1, 0.1)
print(len(a))

#-----------------------------np.linspace--------------------------------------
'''
np.arange(start, stop, step)

np.linspace(start, stop, num)

'''
print('new')
for i in np.linspace(0, 10, 10):
    print(int(i), end = ' ')
print()  
#----------------------------------Срезы--------------------------------------------

A = np.array([[1, 2, 3],[4, 5, 6]])
print(A[1, :])  #[4 5 6]

print(A[:, 1])  #[2 5]

B = A[:, ::-1]
print('A', A)   #A [[1 2 3] / [4 5 6]]

print('B', B)   #B [[3 2 1] / [6 5 4]]

print(A[:,:])   #[[1 2 3] / [4 5 6]]

#-----------------Конец лекции-----------------------------------------------------------------------