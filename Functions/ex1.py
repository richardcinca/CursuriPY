
lista=[]
count=0

while count<5:
    number=input('>>')
    lista.append(int(number))
    count+=1
# print(lista)

#VARIANTA PRIN ACCESARE ELEMENTE LISTA
suma=0
for i in range(0,len(lista)):
    suma=suma+lista[i]
print(f' Total = {suma}')

#VARIANTA PRIN ITERARE SI ADUNARE
# def sum(lista):
#     suma=0
#     for i in lista:
#         suma=suma+i
#     print(suma)


# sum(lista)
    