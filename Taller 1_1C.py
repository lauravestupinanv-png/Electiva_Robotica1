#1C Gráfica de una PT100

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la PT100
R0 = 100
A = 3.9083e-3
B = -5.775e-7

# Rango de temperatura
temperaturas = np.linspace(-200, 200, 401)

# Calcular la resistencia
resistencias = R0 * (1 + A * temperaturas + B * temperaturas**2)

# Crear la gráfica
plt.plot(temperaturas, resistencias)

# Títulos y etiquetas
plt.title("Comportamiento de una PT100")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistencia (Ω)")

# Cuadrícula
plt.grid(True)

# Mostrar gráfica
plt.show()
