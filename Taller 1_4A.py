#4A. PT100

# Datos de la PT100
R0 = 100
A = 3.9083e-3
B = -5.775e-7

# Temperatura
T = 100

# Cálculo de resistencia
R = R0 * (1 + A*T + B*T**2)

print("Temperatura:", T, "°C")
print("Resistencia de la PT100:", R, "ohm")
