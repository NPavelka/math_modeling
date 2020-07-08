print('----------------------------Dop_Zadanie_3-----------------------------')
print('функция определяет по заданным параметрам линзытип изображения и его параметры, где lt - тип линзы (lt=1 - собирающая; lt=2 - рассеивающая); d -  расстояние от предмета до линзы; F - фокусное расстояние.')

def linza(lt=1, d=1, F=1):
    """функция определяет по заданным параметрам линзытип изображения и его параметры,
    где lt - тип линзы (lt=1 - собирающая; lt=2 - рассеивающая);
    d -  расстояние от предмета до линзы;
    F - фокусное расстояние.
    """
    if lt==2:
        print('изображение - прямое, мнимое, уменьшенное')
    elif lt==1:
        if d==F:
            print('изображение нет')
        elif d<F:
            print('изображение - прямое, мнимое, увеличенное')
        elif d>F and d<=2*F:
            print('изображение - обратное, действительное, увеличенное')
        elif d>2*F:
            print('изображение - обратное, действительное, уменьшенное')
        else:
            print('изображение нет')
    else:
        print('изображение нет')
    return lt

lt = int(input('Введите тип линзы (lt=1 - собирающая; lt=2 - рассеивающая): '))
d = float(input('Введите расстояние линзы: '))
F = float(input('Введите фокусное расстояние линзы: '))

linza(lt, d, F)