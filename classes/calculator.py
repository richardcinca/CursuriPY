class Calculator:

    def __init__(self):
        self.a=int(input("a: "))
        self.b=int(input("b: "))
        self.op=input("operatie: ")


    def adunare(self):
        return self.a + self.b

    def scadere(self):
        return self.a-self.b

    def inmultire(self):
        return self.a*self.b

    def impartire(self):
        if self.b==0:
            return 'Error'
        else:
            return self.a/self.b

    def __str__(self):
        if self.op == "+":
            return str(self.adunare())
        elif self.op == "-":
            return str(self.scadere())
        elif self.op == "*":
            return str(self.inmultire())
        elif self.op == "/":
            return str(self.impartire())

obj1=Calculator()
print(obj1)