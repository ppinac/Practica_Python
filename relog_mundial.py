import datetime
#
#poner hora de por lo menos dos lugares mas
# poner formato de fecha como : Monday, Febrary 6, 2019 10:47:04 pm o ama (formato 12 horas)
# poner formato hora como 10:47:04 pm or am (formato 12 horas)
# #
def ver_instrucciones():
    
    print("estas son las operaciones que puedes realizar: ")
    print("1 - ver la hora")
    print("2 - ver la fecha y hora")
    print("3 - ver la hora en Nueva York")
    print("4 - ver la hora en San Francisco")
    print("5 - ver la hora de Hong kong")
    print("6 - ver la hora de Australia")
    print("7 - ver las instrucciones nuevamente")
    print("0 - Salir")

def ver_hora(zona_horaria):
    formato = "%I:%M:%S %p"
    zona_horaria = datetime.timezone(datetime.timedelta(hours= zona_horaria))
    hora_actual = datetime.datetime.now(zona_horaria).time()
    hora_formateada = hora_actual.strftime(formato)
    print("la hora exacta es: {}".format(hora_formateada))

def ver_fecha_hora():
    fecha_actual = datetime.datetime.now().strftime(" %A, %B %d, %Y %I:%M:%S %p")
    print("Hoy es: {}".format(fecha_actual))

    

def ver_reloj():
    print("Bienvenido al Relog Mundial")
    ver_instrucciones()
    while True:
        try:
            operacion =int(input( "Ingrese  la operacion :"))
        except ValueError:
            print("ingrese una opcion valida")
        else:
            if operacion == 1:
               ver_hora(-5)
               
            elif operacion == 2:
                ver_fecha_hora()
            elif operacion ==3:
                ver_hora(-5)
            elif operacion ==4:
                ver_hora(-8)
            elif operacion ==5:
                ver_hora(8)
            elif operacion ==6:
                ver_hora(11)
            elif operacion ==7:
                ver_instrucciones()
            elif operacion ==0:
                print()
                break
            else:
                print("Nose reconoce la Operacion")
                
ver_reloj()