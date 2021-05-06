name=input("\nPlease enter your name: ")
a=input('\n\nPlease type your characters:')

val=0
for var in a:
    if var.isnumeric() == True:
        val=0
    else:
        val=val+1
        break

if val==0 and int(a)%2==0:
    print(f'{name}, your input < {a} > is an int and is an even number')
elif val==0 and int(a)%2!=0:
    print(f'{name}, your input < {a} > is an int and is an odd number')
else:
    print(f'{name}, your input < {a} > is a string')