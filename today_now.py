import datetime

now=datetime.datetime.now()
today =datetime.datetime.today()
fecha_hoy =datetime.datetime.combine(datetime.datetime.today(),datetime.time())

print(now)
print(today)
print(fecha_hoy)
print(fecha_hoy.day)