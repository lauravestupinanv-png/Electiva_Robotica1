#2A. Operaciones con matrices

import numpy as np

# Matrices previamente inicializadas
A = np.array([[3, 6],
              [9, 12]])

B = np.array([[2, 4],
              [6, 8]])

# Suma
suma = A + B

# Resta
resta = A - B

# Multiplicación matricial
multiplicacion = np.dot(A, B)

# División elemento a elemento
division = A / B

print("Matriz A:")
print(A)

print("\nMatriz B:")
print(B)

print("\nSuma:")
print(suma)

print("\nResta:")
print(resta)

print("\nMultiplicación matricial:")
print(multiplicacion)

print("\nDivisión elemento a elemento:")
print(division)
