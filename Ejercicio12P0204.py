# Cálculo de media y desviación típica.
muestra = input("Por favor ingresa una muestra de números separados por comas: ")
muestra = muestra.split(',')
numero = len(muestra)
for i in range(numero):
    muestra[i] = int(muestra[i])
muestra = tuple(muestra)
suma = 0
suma2 = 0
for i in muestra:
    suma += i
    suma2 += i**2
x = suma/numero
ro = (suma2/numero-x**2)**(1/2)
print('La media de la muestra ingresada es', x, ', y la desviación típica es:', ro)