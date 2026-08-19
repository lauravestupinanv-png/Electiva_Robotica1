#3C. Circuito RC

import numpy as np
import matplotlib.pyplot as plt

# Datos ingresados por el usuario
V = float(input("Ingrese el voltaje (V): "))
C_uF = float(input("Ingrese la capacitancia (µF): "))
R = float(input("Ingrese la resistencia (Ω): "))

# Convertir capacitancia de µF a F
C = C_uF * 1e-6

# Constante de tiempo
tau = R * C

# Tiempo de simulación
t = np.linspace(0, 5 * tau, 500)

# Ecuaciones de carga y descarga
Vc_carga = V * (1 - np.exp(-t / tau))
Vc_descarga = V * np.exp(-t / tau)

# Mostrar información
print("\nConstante de tiempo:")
print("τ =", tau, "segundos")

# Gráfica
plt.plot(t, Vc_carga, label="Carga")
plt.plot(t, Vc_descarga, label="Descarga")

plt.title("Carga y descarga de un circuito RC")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje del capacitor (V)")

plt.grid(True)
plt.legend()

plt.show()
