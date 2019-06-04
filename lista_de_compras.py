#Agregar Articulos
#Remover Articulos
#ver Articulos

lista_de_articulos = list()

def agregar_articulo():
    print()
    articulo = input("Nombre del Articulo a Agregar: ")
    lista_de_articulos.append(articulo.capitalize())
    print()
    print("Articulo agregado Correctamente ")
    print()

def remover_articulo():
    print("")
    articulo =input("nombre del articulo a Remover: ")
    lista_de_articulos.remove(articulo.capitalize())
    print("----------------------------------------------")
    print("El Articulo ha sido Removido correctamente")
    print("----------------------------------------------")

def ver_articulo():
    print()
    print("-------------Lista de Compras-------------")
    print("Tienes los siguientes Articulos:")
    for articulo in lista_de_articulos:
        print(articulo)
    print("--------------------------------------------")

print("Bienvenido a Tú lista de Compras")
while True:
    print("Estas son las operaciones que puedes realizar")
    print("1 - Agregar Articulos")
    print("2 - Remover Articulos")
    print("3 - Ver los Articulos")
    print("4 - Salir")
    

    try:
        operacion= int(input("Ingrese la Operacion a Realizar: "))
    
    except ValueError:
        print()
        print("ingrese una Opción Valida")
        print()
    else:
        
        if operacion==1:
            agregar_articulo()
        elif operacion == 2:
            remover_articulo()
        elif operacion == 3:
            ver_articulo()
        else:
            break
print()
print("Gracias por usar nuestra")
print("vuelva pronto")
