def get_input() -> (float,float,str):
    a=float(input("a >> "))
    b=float(input("b >> "))
    operatie=input("operatie >> ")
    return a, b, operatie

def suma(a,b):
    return a+b

def subt(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    try:
        return a/b,"success"
    except ZeroDivisionError:
        return 0, "Division by 0 - error"

def calculator():

    alpha,beta,operation = get_input()
    variabila=""
    if operation=="+":
        variabila=suma(alpha,beta)
        print(variabila)
    elif operation=="-":
        variabila=subt(alpha,beta)
        print(variabila)
    elif operation=="*":
        variabila=mult(alpha,beta)
        print(variabila)
    elif operation=="/":
        variabila=div(alpha,beta)
        print(variabila)
    return variabila


calculator()


