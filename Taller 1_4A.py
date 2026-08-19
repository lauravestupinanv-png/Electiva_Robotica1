#4A. PT100

R0 = 100          # Resistencia a 0 °C (100 ohmios)
A = 3.9083e-3     # Coeficiente A
B = -5.775e-7     # Coeficiente B
C = -4.183e-12    # Coeficiente C

# Temperatura predeterminada
T = 25

# Cálculo de la resistencia usando
# la ecuación de Callendar-Van Dusen

if T >= 0:
    # Para temperaturas iguales o mayores a 0 °C
    R = R0 * (
        1
        + A * T
        + B * T**2
    )

else:
    # Para temperaturas menores a 0 °C
    R = R0 * (
        1
        + A * T
        + B * T**2
        + C * (T - 100) * T**3
    )

# Mostrar el resultado
print(
    f"La resistencia de la RTD PT100 a {T} °C es: "
    f"{R:.4f} ohmios"
)
