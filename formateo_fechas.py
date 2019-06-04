import datetime
now=datetime.datetime.now()

fecha=now.strftime("%B %d,%Y") #mes completo dia y año  ejm: OCtubre 23,2018
print(fecha)
fecha_hora =now.strftime("%B %d, %Y  %H:%M")
print(fecha_hora)
fecha_hora =now.strftime("%B %d, %Y  %I:%M")
print(fecha_hora)
fecha_hora= now.strftime("%A, %d de %B del %Y siendo %H horas con %M minutos")
print(fecha_hora)

fecha_cadena= "22/02/2019"
#fecha_cadena= input("Ingrese la fecha en formato dia/mes/año: ")
fecha_formato = datetime.datetime.strptime(fecha_cadena, "%d/%m/%Y")
print(fecha_formato)