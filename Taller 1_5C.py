#5C. Escribir los nombres en un plot 2D

import matplotlib.pyplot as plt


# NOMBRE: LAURA

# L
plt.plot([0, 0, 2], [3, 0, 0])

# A
plt.plot([3, 4, 5], [0, 3, 0])
plt.plot([3.5, 4.5], [1.5, 1.5])

# U
plt.plot([6, 6, 7, 8, 8], [3, 0, -0.5, 0, 3])

# R
plt.plot([9, 9], [0, 3])
plt.plot([9, 10, 10.5, 9], [3, 3, 1.5, 1.5])
plt.plot([9.5, 10.5], [1.5, 0])

# A
plt.plot([11, 12, 13], [0, 3, 0])
plt.plot([11.5, 12.5], [1.5, 1.5])



# NOMBRE: VALENTINA

# V
plt.plot([0, 1, 2], [-3, -6, -3])

# A
plt.plot([3, 4, 5], [-6, -3, -6])
plt.plot([3.5, 4.5], [-4.5, -4.5])

# L
plt.plot([6, 6, 8], [-3, -6, -6])

# E
plt.plot([9, 9, 11], [-3, -3, -3])
plt.plot([9, 9, 10.5], [-4.5, -4.5, -4.5])
plt.plot([9, 9, 11], [-6, -6, -6])

# N
plt.plot([12, 12, 14], [-6, -3, -6])
plt.plot([14, 14], [-6, -3])

# T
plt.plot([15, 17], [-3, -3])
plt.plot([16, 16], [-3, -6])

# I
plt.plot([18, 19], [-3, -3])
plt.plot([18.5, 18.5], [-3, -6])
plt.plot([18, 19], [-6, -6])

# N
plt.plot([20, 20, 22], [-6, -3, -6])
plt.plot([22, 22], [-6, -3])

# A
plt.plot([23, 24, 25], [-6, -3, -6])
plt.plot([23.5, 24.5], [-4.5, -4.5])



# CONFIGURACIÓN

plt.title("Nombres de los integrantes")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")

plt.show()
