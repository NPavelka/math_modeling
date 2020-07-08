print('----------------------------Dop_Zadanie_2-----------------------------')

def fib(n):
    F_1 = 0
    F_2 = 1
    
    print(F_1, end = ' ')
    print(F_2, end = ' ')
    
    if n % 2 == 0:       
        for i in range(2, n, 2):     
            F_1 = F_1 + F_2
            print(F_1, end = ' ')
            F_2 = F_1 + F_2
            print(F_2, end = ' ')
    elif n % 2 == 1:
        for i in range(1, n, 2):
            F_1 = F_1 + F_2
            F_2 = F_1 + F_2
            if i == n:
                break
            else:
                print(F_1, end = ' ')           
                print(F_2, end = ' ')
    else:
         print('ERROR')  

n = int(input('Введите кол-во чисел в последовательноти: n = '))

fib(n)