# Números ganadores de la loteria primitica.

lista1 = []
lista2 = []
numeros = ""
print("Ingresa los números ganadores de la loteria primitiva y al finalizar teclea s:")

while numeros != "s":
    numeros = input()
    lista1.append(numeros)
lista1.remove("s")

for i in range(len(lista1)):
    lista2.append(int(lista1[i]))

lista2.sort()
print(lista2)

