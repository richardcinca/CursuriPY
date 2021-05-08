item1 = "Afisare lista cumparaturi"
item2 = "Adaugare element"
item3 = "Stergere element"
item4 = "Stergere lista de cumparaturi"
item5 = "Cautare in lista de cumparaturi"

# print(
    
#     f"""
#  MENIU:

#     1 - {item1}
#     2 - {item2} 
#     3 - {item3}
#     4 - {item4}
#     5 - {item5} 

#     """
# )

# command=input("Selecteaza optiunea >> ")
# optiuni=['1','2','3','4','5']

# while command not in optiuni:
#     command=input("\nOptiunea nu este valabila. Selecteaza optiunea >> ")

# if command=='1':
#     print(item1)
# elif command=='2':
#     print(item2)
# elif command=='3':
#     print(item3)
# elif command=='4':
#     print(item4)
# elif command=='5':
#     print(item5)


meniu = {
    "1" : item1,
    "2" : item2,
    "3" : item3,
    "4" : item4,
    "5" : item5
}

print(meniu.keys())

for key,value in meniu.items():
    print("\n",key, ' -- ', value)
command=input("\nPlease select your option:  ")

while command not in meniu.keys():
    command=input("\nPlease select your option:  ")

while command!='q':
    
    command=input("\nPlease select your option:  ")

    if command=='1':
        print(item1)
    elif command=='2':
        print(item2)
    elif command=='3':
        print(item3)
    elif command=='4':
        print(item4)
    elif command=='5':
        print(item5)
        
print(" quited")
    

