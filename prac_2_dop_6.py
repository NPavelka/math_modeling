print('----------------------------Dop_Zadanie_6-----------------------------')
print('Нахождение всех совершенных чисел')

i = int(input('Введите число, до которого будет производиться подчёт: '))  
      
for num in range(2,i,1):

    delit = 2
    D = [1]
#    print('new')   
       
    while delit < num:
            
        if num % delit == 0:
            D.append(delit)
            
        else:
            None 
            
        delit = delit + 1

    S = sum(D)
    
    if num % S == 0 and S != 1:
        print(num, sep = ' ')
        
    else:
        None 
        
#    print(num)
#    print(D)
#    print(S)
#print('end')                















