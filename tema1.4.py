


numar=input("\nnumber>> ")

while True:
    try:
        if float(numar)<0:
            numar=-1*int(numar)
            print(f"\nnumarul a fost transformat in {int(numar)}")
            break
        elif float(numar)==0:
            print("\nnumarul este 0")
            break
        elif float(numar) in range(0,10):
            print(f"\nnumarul {int(numar)} este pozitiv, mai mic decat 10")
            break
        else:
            print("\nOut of range")
            numar=float(input("\ninsert number>> "))
            
    except ValueError:
        numar=input("\nInput gresit, insert number>> ")