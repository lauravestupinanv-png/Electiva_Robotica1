#2C. Sistema de segundo orden

import numpy as np
import matplotlib.pyplot as plt

# Ingresar parámetros
wn = float(input("Ingrese la frecuencia natural wn: "))
zeta = float(input("Ingrese el factor de amortiguamiento zeta: "))

# Tiempo
t = np.linspace(0, 10, 1000)

# Respuesta del sistema
if 0 < zeta < 1:

    wd = wn * np.sqrt(1 - zeta**2)

    y = 1 - (
        np.exp(-zeta * wn * t) *
        (
            np.cos(wd * t)
            + (zeta / np.sqrt(1 - zeta**2)) * np.sin(wd * t)
        )
    )

    tipo = "Subamortiguado"

elif zeta == 1:

    y = 1 - (1 + wn * t) * np.exp(-wn * t)

    tipo = "Críticamente amortiguado"

elif zeta > 1:

    r1 = -wn * (zeta - np.sqrt(zeta**2 - 1))
    r2 = -wn * (zeta + np.sqrt(zeta**2 - 1))

    y = 1 + (
        r2 * np.exp(r1 * t) -
        r1 * np.exp(r2 * t)
    ) / (r1 - r2)

    tipo = "Sobreamortiguado"

else:
    print("El factor de amortiguamiento debe ser mayor que 0.")
    tipo = "Valor no válido"

# Mostrar tipo de sistema
print("\nTipo de sistema:", tipo)

# Gráfica
plt.plot(t, y)

plt.title("Respuesta de un sistema de segundo orden")
plt.xlabel("Tiempo (s)")
plt.ylabel("Respuesta")

plt.grid(True)
plt.show()
