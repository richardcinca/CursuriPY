
try:
    f=open('file.txt')
    #var = bar_bad
except FileNotFoundError:
    print("Sorry. This file doesn't exist")
except NameError as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    #Closes the "trial" to release memory
    print("Executing Finally...")