'''
Подробное описание данного алгоритма находится по ссылке:
https://habr.com/ru/post/427333/).
'''


def kelvin_to_color(Kel=10000):
    ''' Функция возвращающая цвет (в RGB форме) цвезды, по температуре
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