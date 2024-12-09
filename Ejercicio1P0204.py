# Lista de asignaturas.

lista = [] 
asignatura = ""
print("Ingresa las asignaturas del curso, al finalizar teclea salir:")

while asignatura != "salir":
    asignatura = str(input())
    lista.append(asignatura)
lista.remove("salir")
print ("Esta es la lista de las asignaturas de este curso:")
print(lista)