"""
preiau anul
atata timp cat anul nu este numar
    daca anul este bisect
        printez "DA"
    daca anul nu este bisect
        printez nu
    altfel
        preiau anul
    
"""

anul=input("Introdu anul >> ")

while anul.isnumeric() == False:
    anul=input("Caracterele nu sunt numerice. Try again >> ")
    if anul.isnumeric() == True:
        if int(anul)%4 == 0:
            print(f'Anul <{anul}> este bisect')
            break
        else:
            print(f'Anul <{anul}> nu este bisect')
            break
        



    
    
    
