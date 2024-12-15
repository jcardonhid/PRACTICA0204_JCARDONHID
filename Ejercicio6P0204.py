# Asignaturas reprobadas.

asignaturas = ["Matemáticas", "Lengua", "Ciencias", "Historia", "Inglés"]
notas = []
print("Por favor ingresa la nota que tienes en cada una de las asignaturas:")

for i in range(len(asignaturas)):
    notas.append(int(input(asignaturas[i])))

for i in range(len(notas)):
    if notas[i] < 5:
        print("Debes repetir: " + asignaturas[i])