# C4. SISTEMA DE COORDENADAS X, Y, Z

import matplotlib.pyplot as plt

print(" SISTEMA DE COORDENADAS 3D")


# Ingresar coordenadas del vector
x = float(input("Ingrese la coordenada X del vector: "))
y = float(input("Ingrese la coordenada Y del vector: "))
z = float(input("Ingrese la coordenada Z del vector: "))


# Crear figura 3D
fig = plt.figure(figsize=(8, 8))

ax = fig.add_subplot(
111,
projection="3d"
)


# Tamaño de los ejes
limite = max(
abs(x),
abs(y),
abs(z),
1
) + 2


# EJES X, Y Y Z


# Eje X
ax.plot(
[-limite, limite],
[0, 0],
[0, 0]
)

# Eje Y
ax.plot(
[0, 0],
[-limite, limite],
[0, 0]
)

# Eje Z
ax.plot(
[0, 0],
[0, 0],
[-limite, limite]
)

# VECTOR


ax.quiver(
0,
0,
0,
x,
y,
z,
arrow_length_ratio=0.1
)


# Punto final del vector
ax.scatter(
x,
y,
z
)


# Mostrar coordenadas del punto final
ax.text(
x,
y,
z,
f"({x}, {y}, {z})"
)


# CONFIGURACIÓN


ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Valores positivos y negativos
ax.set_xlim(
-limite,
limite
)

ax.set_ylim(
-limite,
limite
)

ax.set_zlim(
-limite,
limite
)

# Quitar cuadrícula
ax.grid(False)

ax.set_title(
"Sistema de coordenadas X, Y, Z y vector"
)

plt.show()
