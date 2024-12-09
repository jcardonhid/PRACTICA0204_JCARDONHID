# Notas de Asignaturas.

lista = []
lista2 = []
notas = []
asignatura = ""
print("Ingresa las asignaturas del curso, al finalizar teclea salir:")

while asignatura != "salir":
    asignatura = str(input())
    lista.append(asignatura)
lista.remove("salir")

for i in range(len(lista)):
    if i == 0:
        print("ingresa la nota en entero obtenida en:", lista[i])
        notas = (input())
        lista2.append(notas)
    elif i > 0:
        print("ingresa la nota en entero obtenida en:", lista[i])
        notas = (input())
        lista2.append(notas)

for i in range(len(lista)):
    if i == 0:
        print("la nota obtenida en", lista[i], "es:", lista2[i])
    elif i > 0:
        print("la nota obtenida en", lista[i], "es:", lista2[i])