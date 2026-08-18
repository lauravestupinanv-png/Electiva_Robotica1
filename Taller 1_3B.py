#3B. Volúmenes

import math

print("===== CÁLCULO DE VOLÚMENES =====")
print("1. Prisma")
print("2. Pirámide")
print("3. Cono truncado")
print("4. Cilindro")

opcion = int(input("Seleccione el sólido (1-4): "))

if opcion == 1:
    # Prisma
    area_base = float(input("Ingrese el área de la base: "))
    altura = float(input("Ingrese la altura: "))

    volumen = area_base * altura

    print("El volumen del prisma es:", volumen)

elif opcion == 2:
    # Pirámide
    area_base = float(input("Ingrese el área de la base: "))
    altura = float(input("Ingrese la altura: "))

    volumen = (area_base * altura) / 3

    print("El volumen de la pirámide es:", volumen)

elif opcion == 3:
    # Cono truncado
    radio_mayor = float(input("Ingrese el radio mayor: "))
    radio_menor = float(input("Ingrese el radio menor: "))
    altura = float(input("Ingrese la altura: "))

    volumen = (math.pi * altura / 3) * (
        radio_mayor**2 +S
        radio_mayor * radio_menor +
        radio_menor**2
    )

    print("El volumen del cono truncado es:", volumen)

elif opcion == 4:
    # Cilindro
    radio = float(input("Ingrese el radio: "))
    altura = float(input("Ingrese la altura: "))

    volumen = math.pi * radio**2 * altura

    print("El volumen del cilindro es:", volumen)

else:
    print("Opción no válida.")
