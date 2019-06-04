
def realizar_operaciones(operacion,a,b):
    if operacion == 1:
        return a+b
    elif operacion == 2:
        return a-b
    elif operacion == 3:
        return a*b
    elif operacion == 4:
        return a/b


print("Bienvenidos a la Calculadora")
while True:
    print("estas son las operaciones que puedes realizar:")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicación")
    print("4 - División")

    try:
        operacion =int(input("Introduce el numero de operacion que quieres realizar: "))
        if operacion < 1 or operacion > 4:
            print("")
            print("Numero ingresado invalido!!. Ingrese un numero de operacion valido")
            print()
            print()
            continue
        a = int(input("Introduce el primer numero "))
        b = int(input("Introduce el segundo numero "))
            
    except ValueError:
        print()
        print("El numero ingresado no es un numero valido. vuelva a ingresar")
        print()
    else: 
        resultado = realizar_operaciones(operacion,a,b)
        print("el resultado es "+ str(resultado))
        continuar = input("Deseas continuar?  si/no  ")
        if continuar != "si":
            break 
print("gracias por usar nuestra calculadora")
 
