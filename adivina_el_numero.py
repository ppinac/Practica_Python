import random
#darle 5 vidad al usuario
#dar pistas, si el numero es mayor o menor
#poner la opcion de volver a jugar genernando otro numero

def jugar():
    intentos=0
    numero_aleatorio = random.randint(1,10)
    print("Bienvenido a adivina el numero")
    print("estoy pensando un numero del 1 al 10")
    print("Solo tienes 5 intentos")
    print("Adivina cual es")
    while intentos < 5:
        adivinanza = int(input("El numero es: "))

        if adivinanza == numero_aleatorio:
            print("Adivinaste!!")
            jugar_nuevamente = input("Jugar de nuevo? si/no: ")
            if jugar_nuevamente.lower()== "si":
                jugar()
            break
        elif numero_aleatorio > adivinanza:
            print("Fallaste, mi numero es mayor")
        else:
            print("Fallaste, mi numero es mayor")
        intentos += 1
        #print("te quedan: "+ str(5-intentos)+" Intentos")
        print("Intentos {}/5".format(intentos))
    

    else:
        print()
        print("Se te acabaron los intentos")
        print("Gracias por jugar")
        print("---------------------------------------------------------------")
        jugar_nuevamente = input("Jugar de nuevo? si/no: ")

        if jugar_nuevamente.lower()== "si":
            jugar()
jugar() 