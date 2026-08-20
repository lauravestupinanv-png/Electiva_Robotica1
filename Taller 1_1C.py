# C1. GRAFICA DE UNA PT100

import numpy as np
import matplotlib.pyplot as plt

# Datos de la PT100
R0 = 100

A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12

# Temperatura desde -200 °C hasta 200 °C
temperaturas = np.linspace(-200, 200, 401)

# Lista para guardar las resistencias
resistencias = []

# Calcular la resistencia para cada temperatura
for T in temperaturas:

    # Primera ecuación: T >= 0 °C
    if T >= 0:

        R = R0 * (
            1
            + A * T
            + B * T**2
        )

    # Segunda ecuación: T < 0 °C
    else:

        R = R0 * (
            1
            + A * T
            + B * T**2
            + C * (T - 100) * T**3
        )

    resistencias.append(R)


# GRAFICA

plt.figure()

plt.plot(
    temperaturas,
    resistencias
)

plt.title(
    "Comportamiento de una PT100"
)

plt.xlabel(
    "Temperatura (°C)"
)

plt.ylabel(
    "Resistencia (Ω)"
)

plt.grid(True)

plt.show()
