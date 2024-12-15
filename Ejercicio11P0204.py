# Multiplicador de matrices.

matrix1 = ((1, 2, 3), (4, 5, 6))
matrix2 = ((-1, 0), (0, 1), (1,1))
resultado = [[0, 0], [0, 0]]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            resultado[i][j] += matrix1[i][k] * matrix2[k][j]
for i in range(len(resultado)):
    resultado[i] = tuple(resultado[i])
resultado = tuple(resultado)
for i in range(len(resultado)):
    print(resultado[i])