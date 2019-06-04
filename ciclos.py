manzanas = 10
while manzanas >0:
    print("Me estoy comiendo una manzana " + str(manzanas))
    manzanas-=1
print("me quede sin manzana")

lista_numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in lista_numeros:
    if numero ==5:
        continue
    print(numero)

vocales = "aeiou"
lista_vocales= list(vocales)
for vocales in lista_vocales:
    if vocales =="U":
        continue
    print(vocales.upper())