numeros = [0,1,2,3,4,5,6,7,8,9,10]
print(numeros)
print(numeros[1])

print(numeros[0:6])
print(numeros[0:7])
print(numeros[0:1])
print(numeros[0:11])
print(numeros[0:9999])

print(numeros[0:])
print(numeros[:2])
print(numeros[:])

print(numeros[-6:-3])
print(numeros[-6:])
print(numeros[:-3])

print("steps")

print(numeros[::2])
print(numeros[::3])
print(numeros[2:8:2]) #2 inicio  8 final del slices y 2 saltos
print(numeros[::-1]) #recorrido de forma contraria
print(numeros[-2:-5:-1]) #recorrido con indices negativos

print("borrar o reemplazar elemento de lista con rebanadas")
del numeros[0]
print(numeros)

del numeros[0:4]
print(numeros)

del numeros[2:4]
print(numeros)

numeros[1:2] = [6,7,8]
print(numeros)

numeros[4:]= [80,80]
print(numeros)

numeros[4:]= [9,10]
print(numeros)