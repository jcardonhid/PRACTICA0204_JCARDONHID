# Cambiar el orden de una lista.

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = []

for i in range(1,len(lista1)+1):
    lista2.append(lista1[i*-1])

for i in lista2:
    if i != 1:
        print(i, end=", ")
    elif i == 1:
        print(i)