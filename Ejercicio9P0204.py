# Tipo y número de vocales en una palabra.

palabra1 = str(input("Por favor ingresa una palabla:"))
lista1 = list(palabra1)

print("la palabra", palabra1, "contiene:\n", lista1.count("a"), "- A\n", lista1.count("e"), "- E\n",
      lista1.count("i"), "- I\n", lista1.count("o"), "- O\n", lista1.count("u"), "- U\n")