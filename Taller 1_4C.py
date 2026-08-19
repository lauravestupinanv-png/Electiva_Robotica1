#4C. Sistema coordenado X, Y, Z

import numpy as np
import matplotlib.pyplot as plt

# Ingresar coordenadas del vector
x = float(input("Ingrese la coordenada X: "))
y = float(input("Ingrese la coordenada Y: "))
z = float(input("Ingrese la coordenada Z: "))

# Crear figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Tamaño de los ejes
limite = max(abs(x), abs(y), abs(z)) + 2

# Ejes X, Y y Z
ax.plot([0, limite], [0, 0], [0, 0])
ax.plot([0, 0], [0, limite], [0, 0])
ax.plot([0, 0], [0, 0], [0, limite])

# Vector desde el origen hasta (x,y,z)
ax.quiver(0, 0, 0, x, y, z)

# Punto final del vector
ax.scatter(x, y, z)

# Etiquetas de los ejes
ax.set_xlabel("X")S
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Límites
ax.set_xlim(0, limite)
ax.set_ylim(0, limite)
ax.set_zlim(0, limite)

# Título
ax.set_title("Sistema de coordenadas 3D y vector")

plt.show()
