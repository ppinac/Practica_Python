import re

archivo = open("ejemplo.txt",)

info= archivo.read()
archivo.close()
print(info)

#print(re.match(r"abcdefghijklmnñopqrstuv",info)) MATCH SOLO BUSTA EN LA PRIMERA LINEA
#print(re.search(r"0123456789",info)) ## USANDO SEARCH SI PODEMOS BUSCAR EN TODO EL DOCUMENTO pero solo el  pri,er match
print(re.search(r"\+\d-\(\d{3}\)-\(\d{3}\)-\(\d{4}\)",info)) # la expresion regular debe estar tal como buscamos
print(re.search(r"\+\d-\(?\d{3}\)?-\(?\d{3}\)?-\(?\d{4}\)?",info)) #parentesis opcionales
print(re.search(r"\+\d-[-\(\d\)]+",info))## solo encuentra el primer matrch
print(re.findall(r"\+\d-[-\(\d\)]+",info)) ## findall busca todos los match  que se encuentra en