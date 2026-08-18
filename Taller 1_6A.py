#6A. Fuerza de un cilindro neumático de doble efecto

import math

# Datos del cilindro
presion_bar = 6       # Presión en bar
diametro_piston = 50  # Diámetro del pistón en mm
diametro_vastago = 20 # Diámetro del vástago en mm

# Conversión de unidades
presion_pa = presion_bar * 100000
diametro_piston_m = diametro_piston / 1000
diametro_vastago_m = diametro_vastago / 1000

# Área del pistón
area_piston = math.pi * diametro_piston_m**2 / 4

# Área del vástago
area_vastago = math.pi * diametro_vastago_m**2 / 4

# Fuerza de avance
fuerza_avance = presion_pa * area_piston

# Fuerza de retroceso
fuerza_retroceso = presion_pa * (area_piston - area_vastago)

# Resultados
print("Presión:", presion_bar, "bar")
print("Diámetro del pistón:", diametro_piston, "mm")
print("Diámetro del vástago:", diametro_vastago, "mm")

print("\nÁrea del pistón:", area_piston, "m2")
print("Área del vástago:", area_vastago, "m2")

print("\nFuerza de avance:", round(fuerza_avance, 2), "N")
print("Fuerza de retroceso:", round(fuerza_retroceso, 2), "N")
