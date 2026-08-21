# C2. FUNCIÓN DE TRANSFERENCIA DE SEGUNDO ORDEN

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


print(" SISTEMA DE SEGUNDO ORDEN")


print("\nFunción de transferencia:")
print(" b1*s + b0")
print("G(s) = - - - - - - - - -")
print(" a2*s²+a1*s+a0")


# INGRESO DE COEFICIENTES


print("\nIngrese los coeficientes del numerador:")

b1 = float(input("b1 = "))
b0 = float(input("b0 = "))

print("\nIngrese los coeficientes del denominador:")

a2 = float(input("a2 = "))
a1 = float(input("a1 = "))
a0 = float(input("a0 = "))


# VERIFICAR QUE SEA DE SEGUNDO ORDEN


if a2 == 0:

    print("\nError: a2 no puede ser cero.")
    print("El denominador debe ser de segundo orden.")

else:


    # FUNCIÓN DE TRANSFERENCIA


    numerador = [b1, b0]

    denominador = [a2, a1, a0]

    sistema = signal.TransferFunction(
        numerador,
        denominador
    )


    # NORMALIZAR DENOMINADOR


    a1_n = a1 / a2
    a0_n = a0 / a2


    # FRECUENCIA NATURAL Y FACTOR DE AMORTIGUAMIENTO


    if a0_n > 0:

        wn = np.sqrt(a0_n)

        zeta = a1_n / (2 * wn)

    else:

        wn = np.nan
        zeta = np.nan


    # POLOS


    polos = np.roots(denominador)


    # GANANCIA ESTÁTICA


    if a0 != 0:

        ganancia_estatica = b0 / a0

    else:

        ganancia_estatica = np.nan



    # TIPO DE SISTEMA


    if np.isnan(zeta):

        tipo = "Sistema no estable"

    elif zeta < 0:

        tipo = "Sistema inestable"

    elif np.isclose(zeta, 0):

        tipo = "Sin amortiguamiento"

    elif zeta < 1:

        tipo = "Subamortiguado"

    elif np.isclose(zeta, 1):

        tipo = "Críticamente amortiguado"

    else:

        tipo = "Sobreamortiguado"


    # MOSTRAR RESULTADOS
    print(" RESULTADOS")

    print("\nCoeficientes del numerador:")
    print(numerador)

    print("\nCoeficientes del denominador:")
    print(denominador)

    print("\nPolos del sistema:")
    print(polos)

    print("\nGanancia estática (K):")
    print(ganancia_estatica)

    if not np.isnan(wn):

        print("\nFrecuencia natural (wn):")
        print(wn)

        print("\nFactor de amortiguamiento (zeta):")
        print(zeta)

        print("\nTipo de sistema:")
        print(tipo)


    # RESPUESTA AL ESCALÓN

    tiempo, respuesta = signal.step(
        sistema
    )

    # GRÁFICA

    plt.figure()

    plt.plot(
        tiempo,
        respuesta
    )

    plt.title(
        "Respuesta al escalón - Sistema de segundo orden"
    )

    plt.xlabel(
        "Tiempo (s)"
    )

    plt.ylabel(
        "Respuesta"
    )

    plt.grid(True)

    plt.show()
