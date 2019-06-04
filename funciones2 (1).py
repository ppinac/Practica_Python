
def pedir_pizza():
    print("Pedir pizza")
pedir_pizza()

def checar_entrada(edad):
    if edad < 18:
        print("no puedes entrar al bar y tampoco puedes beber".upper())
    elif edad >= 18:
        print("puedes entrar al bar y tambien puede beber")
    else:
        print("puedes entrar al bar pero no puedes beber")

edad = 21
edad_2 = 17

checar_entrada(edad)
checar_entrada(edad_2)

