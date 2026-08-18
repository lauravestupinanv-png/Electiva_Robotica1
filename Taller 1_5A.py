#5A. Matrices de rotación

import numpy as np

# Rotación alrededor del eje X
def rotacion_x(angulo):
    theta = np.radians(angulo)

    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

    return Rx


# Rotación alrededor del eje Y
def rotacion_y(angulo):
    theta = np.radians(angulo)

    Ry = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

    return Ry


# Rotación alrededor del eje Z
def rotacion_z(angulo):
    theta = np.radians(angulo)

    Rz = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

    return Rz


# Ángulo de prueba
angulo = 90

# Obtener las matrices
Rx = rotacion_x(angulo)
Ry = rotacion_y(angulo)
Rz = rotacion_z(angulo)

# Mostrar resultados
print("Rotación en X:")
print(np.round(Rx, 3))

print("\nRotación en Y:")
print(np.round(Ry, 3))

print("\nRotación en Z:")
print(np.round(Rz, 3))
