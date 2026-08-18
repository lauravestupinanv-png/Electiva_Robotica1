#4B. Tipos de robots

print(" TIPOS DE ROBOT ")
print("1. Robot Cilíndrico")
print("2. Robot Cartesiano")
print("3. Robot Esférico")

opcion = int(input("Seleccione un tipo de robot (1-3): "))

if opcion == 1:
    print("\nTipo: Robot Cilíndrico")
    print("Número de articulaciones: 3")

elif opcion == 2:
    print("\nTipo: Robot Cartesiano")
    print("Número de articulaciones: 3")

elif opcion == 3:
    print("\nTipo: Robot Esférico")
    print("Número de articulaciones: 3")

else:
    print("\nOpción no válida.")
