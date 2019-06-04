lista_calificaciones= [9,10,6,5]
print(lista_calificaciones)
diccionario_calificaciones = {"Pablo":9,"Aldo":10,"Juan":6,"Kevin":5}
print(diccionario_calificaciones)
print(diccionario_calificaciones["Aldo"])
a=dict([["pepe",7],["maria",4]])
print(a)
#diccionario
dias_semana = {"lunes":9,"martes":10,"miercoles":11}
print(dias_semana)
dias_semana["jueves"]=12
print(dias_semana)
dias_semana.update({"viernes":13,"viernes":13,"sabado":14})
print(dias_semana)
dias_semana.update({"domingo":16})
print(dias_semana)

for dias in dias_semana:
    print(dias)

for dias in dias_semana:
    print(dias_semana[dias])

for key in dias_semana.keys():
    print(key)

for value in dias_semana.values():
    print(value)

for item in dias_semana.items():
    print(item)
