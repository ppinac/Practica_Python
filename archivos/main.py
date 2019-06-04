


def agregar_articulo(articulo):
    archivo_lista = open("lista.txt","a")

    archivo_lista.write("{}\n".format(articulo))

    archivo_lista.close()

def listar_articulo():
    archivo = open("lista.txt","r")
    leer =archivo.read()
    archivo.close()
    print(leer)
while True:
    print("Bienvenidos a la gestion de Articulos")
    print("1 - Agregar Articulos")
    print("2 - Ver los Articulos")
    print("3 - Salir")
    try:
        opcion = int(input("Ingrese la opcion a realizar: "))
    except ValueError:
        print("ingrese un opcion valida")
        

    else:
        if opcion == 1:
            print("----------------------------------------------")
            agregar_articulo(input("Articulo que quieres agregar: "))
        elif opcion == 2:
            print("-----------------------------------------------")
            listar_articulo()
        elif opcion == 3:
            break
        else:
            print("ingrese una opcion valida")
