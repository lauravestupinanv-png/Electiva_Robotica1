#2B. Números aleatorios

import random

# Datos ingresados por el usuario
cantidad = int(input("¿Cuántos números aleatorios desea generar?: "))
inicio = int(input("Ingrese el valor inicial del rango: "))
fin = int(input("Ingrese el valor final del rango: "))

# Generar números aleatorios
numeros = []

for i in range(cantidad):
    numero = random.randint(inicio, fin)
    numeros.append(numero)

# Mostrar resultados
print("\nNúmeros aleatorios generados:")
print(numeros)
