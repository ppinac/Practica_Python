#agregar contactos
#remover contactos
#actualizar contactos
#ver un contactos
#vertodos los contactos

agenda_telefonica = dict()
def imprimir_operacion(nombre_operacion):
    print()
    print("------------------------------------------")
    print(nombre_operacion)
    print("------------------------------------------")

def agregar_contacto():
    nombre = input("Nombre del nuevo contacto: ")
    numero = input("Numero del nuevo contacto: ")
    agenda_telefonica[nombre]= numero
    imprimir_operacion("Contacto Agregado")
    
def remover_contacto():
    nombre_operacion = None
    nombre =input("nombre del contacto que deseas borrar: ")
    try:    
        del agenda_telefonica[nombre]
    except KeyError:
        nombre_operacion= "Ese contacto no exite"
    else:    
        nombre_operacion = "Contacto borrado"
    imprimir_operacion("Contacto Borrado")

def actualizar_contacto():
    nombre_operacion = None
    nombre= input("nombre del contacto que deseas actualizar: ")
    for nombre in agenda_telefonica:
        numero = input("ingrese el nuevo numero de este contacto: ")
        agenda_telefonica[nombre]= numero
        nombre_operacion = "Contacto Actualizado"
    
    nombre_operacion = "El contacto no Existe"
    imprimir_operacion(nombre_operacion)

def ver_contacto():
    nombre_operacion = None
    nombre =input("nombre del contacto: ")
    

    try:
        nombre_operacion = "{} -{}".format(nombre,agenda_telefonica[nombre])
    except (KeyError, TypeError):
        nombre_operacion ="Contacto no existe"

    imprimir_operacion(nombre_operacion)

def vertodos_contacto():
    nombre_operacion = None
    if len(agenda_telefonica)==0:
        nombre_operacion ="aun no ha registrado ningun contacto"
    else:
        for contacto in agenda_telefonica:
           # print(contacto + " - " + agenda_telefonica[contacto])
            if nombre_operacion == None:
                nombre_operacion = "{} - {}".format(contacto,agenda_telefonica[contacto])
            else:
                nombre_operacion += "\n {} - {}".format(contacto,agenda_telefonica[contacto])
    imprimir_operacion(nombre_operacion)   

def iniciar_agenda():
    print("Bienvenido a la Agenda Telefonica ")
    while True:
        print("1 - Agregar un contacto")
        print("2 - Remover Contacto")
        print("3 - Actualizar Contacto")
        print("4 - Ver un Contacto")
        print("5 - Ver todos los contactos")
        print("6 - Salir")
    
        try:
            operacion= int(input("Ingrese la Operacion a realizar:"))
        except ValueError:
            print("------------------------------------")
            print("Ingrese una opcion valida")
            print("Ingresa  un numero del 1 al 6")
            print("------------------------------------")
        else:
            if operacion == 1:
                agregar_contacto()
            elif operacion == 2:
                remover_contacto()
            elif operacion == 3:
                actualizar_contacto()
            elif operacion == 4:
                ver_contacto()
            elif operacion == 5:
                vertodos_contacto()
            elif operacion ==6:
                break
            else:
                print("operacion desconocida")
                break
def despedida():
    print("Gracias por usar la agenda")

iniciar_agenda()
despedida()
            
