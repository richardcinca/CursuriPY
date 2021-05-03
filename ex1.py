while True:
    euro = input("Valoare euro pentru convertire: ")
    if euro.isdigit():
        euro=int(euro)
        print("Valoarea convertita este",euro*4.9,"RON")
    else:
        print("Valoarea introdusa nu este numar")
    quit = input("Apasa 'q' pentru a iesi sau orice tasta pentru a repeta procesul de conversie:")
    if quit.upper() == "Q":
        break
    else:
        pass