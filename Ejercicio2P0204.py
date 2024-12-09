# Asignaturas que Estudias.

lista = [] 
asignatura = ""
print("Ingresa las asignaturas del curso, al finalizar teclea salir:")

while asignatura != "salir":
    asignatura = str(input())
    lista.append(asignatura)
lista.remove("salir")

for i in range(len(lista)):
    if i == 0:
        print("Yo estudio:", lista[i])
    elif i > 0:
        print("Yo estudio:", lista[i])