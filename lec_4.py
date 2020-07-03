print('--------------------------------Функции--------------------------------')
print('--------------------------------Создание функции--------------------------------')
'''
def name_func (arg1, arg2):              #Заголовок функции
    instruction1 = arg1 + arg2
    ...
                                         #Тело функции 
                                         
    return instruction1                  #Возврат результата функции
'''

def mult_func(a):              
    x = a * 3
    return x

tmp = mult_func(1)
print(tmp)

print(mult_func('Good'))

print('--------------------------------Область видимости--------------------------------')

x0 = 10

def move(t):
    x = x0 * t
    return x

print(move(3))
'''
print(x)                                #Тело х не задано
'''

x = 'Good'

def my_func():
    x = 'Bad'
    print(x)
    
my_func()
print(x)

print('--------------------------------Аргументы--------------------------------')

def changer(a, b):                      #В аргументах передаются ссылки на объекты (значения функций нужны всегда)
    a = 2                               #Изменяется только значение локального имени
    b[0] = 'Good'                       #Изменяется непосредственно разденяемый объект
    return a

x = x = 10
L = [1, 2]

changer(x, L)                           #Передаются изменяемый (L) и неизменяемый (x) объекты
print(x)                                #Неизменяемый объект остаётся неизменяемым

print(L)                                #Изменяемый объект меняется

L = [1, 2]
changer(x, L[:])
print(L) 

def my_func(a=1, b=0):                  #Определение значений аргументов по умолчанию
    x = 3*a - b
    return x
print(my_func())

print('--------------------------------Описание функции--------------------------------')

def crutoi_chuvak(a=1, b=1, c=1):
    """ Мотивирующая функция, возвращающая всегда значение
        'Крутой чувак', независимо от того какие аргументы
        Вы в неё запихали
    """
    a = 'Pofig'
    b = 'Pofig'
    print('Крутой чувак')
    return a, b

help(crutoi_chuvak)

print('--------------------------------Примеры функций (их нет)--------------------------------')