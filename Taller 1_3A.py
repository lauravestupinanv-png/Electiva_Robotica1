#3A. Coordenadas rectangulares a cilíndricas y esféricas

import math

# Coordenadas rectangulares
x = 3
y = 4
z = 5

# COORDENADAS CILÍNDRICAS
r = math.sqrt(x**2 + y**2)

theta = math.atan2(y, x)

# Convertir de radianes a grados
theta_grados = math.degrees(theta)

# COORDENADAS ESFÉRICAS
rho = math.sqrt(x**2 + y**2 + z**2)

theta_esfericas = math.atan2(y, x)

phi = math.acos(z / rho)

# Convertir ángulos a grados
theta_esfericas_grados = math.degrees(theta_esfericas)
phi_grados = math.degrees(phi)

# RESULTADOS

print("Coordenadas rectangulares:")
print("x =", x)
print("y =", y)
print("z =", z)

print("\nCoordenadas cilíndricas:")
print("r =", r)
print("theta =", theta_grados, "grados")
print("z =", z)

print("\nCoordenadas esféricas:")
print("rho =", rho)
print("theta =", theta_esfericas_grados, "grados")
print("phi =", phi_grados, "grados")
