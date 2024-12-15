# Palabra palíndromo.

palabra = str(input("Ingresa una palabra:"))
lista1 = list(palabra)
lista2 = list(palabra)
lista2.reverse()

if lista1 == lista2:
    print("Es una palabra políndromo")
else:
    print("No es una palabra políndromo")