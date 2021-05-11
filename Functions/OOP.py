class Malware:
    species='Virus'


    def __init__(self,name,family):
        self.name=name
        self.type=family
        self.state='Idle'

    def command(self,option):
        if option == "Infect":
            self.state="Infecting target"
            print(self.state)
        elif option == "Off":
            self.state="Shuting down target"

wacatac=Malware("Wacatac","Trojan")

wacatac.command(input("Command >> "))

