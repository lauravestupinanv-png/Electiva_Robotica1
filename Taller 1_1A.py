#1A. Operaciones con dos vectores

import numpy as np

# Vectores previamente inicializados
A = np.array([2, 4, 6])
B = np.array([1, 3, 5])

# Suma
suma = A + B

# Resta
resta = A - B

# Producto punto
producto_punto = np.dot(A, B)

# Producto cruz
producto_cruz = np.cross(A, B)

# División elemento a elemento
division = A / B

# Mostrar resultados
print("Vector A:", A)
print("Vector B:", B)
print("Suma:", suma)
print("Resta:", resta)
print("Producto punto:", producto_punto)
print("Producto cruz:", producto_cruz)
print("División:", division)
