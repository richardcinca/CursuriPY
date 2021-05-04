#x=()
#x=(True,False,2,8,1,"text",("tuple",2))+(1,2,3)
#print(x,type(x))

items = None
if not items:
    print("Your backpack is empty")

items = ("food","knife","socks","jacket")

print("\n Your item tuple is: {}\n".format(items))

for item,value in enumerate(items):
    print("Item no.{} - {}".format(item,value))

print("\n\nYour backpack contains {} items".format(len(items)))

print(input("\n\nPress <enter> to exit"))