# C6. CONTORNOS DE DOS LOGOS DE AUTOMÓVILES
# ============================================================

import cv2
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# LOGO MAZDA
# ============================================================

print("\n========== C6. LOGO MAZDA ==========")

imagen_mazda = cv2.imread("Mazda.jpg")

if imagen_mazda is None:

    print("Error: no se encontró el archivo Mazda.jpg")

else:

    # Convertir a escala de grises
    gris_mazda = cv2.cvtColor(
        imagen_mazda,
        cv2.COLOR_BGR2GRAY
    )

    # Detectar bordes
    bordes_mazda = cv2.Canny(
        gris_mazda,
        80,
        180
    )

    # Obtener los contornos
    contornos_mazda, _ = cv2.findContours(
        bordes_mazda,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_NONE
    )

    # Ordenar de mayor a menor
    contornos_mazda = sorted(
        contornos_mazda,
        key=cv2.contourArea,
        reverse=True
    )

    # Seleccionar contornos importantes
    contornos_mazda = [
        c
        for c in contornos_mazda
        if cv2.contourArea(c) > 1000
    ]

    # Mostrar coordenadas X y Y
    for i, contorno in enumerate(
        contornos_mazda[:10]
    ):

        puntos = contorno[:, 0, :]

        x = puntos[:, 0]

        y = -puntos[:, 1]

        print(
            f"\nContorno Mazda {i + 1}"
        )

      


    # Graficar los contornos
    plt.figure(
        figsize=(10, 6)
    )

    for contorno in contornos_mazda[:10]:

        puntos = contorno[:, 0, :]

        x = puntos[:, 0]

        y = -puntos[:, 1]

        plt.plot(
            x,
            y
        )

    plt.title(
        "Contornos del logo Mazda"
    )

    plt.xlabel("X")

    plt.ylabel("Y")

    plt.axis("equal")

    plt.grid(True)

    plt.show()


# ============================================================
# LOGO BMW
# ============================================================

print("\n========== C6. LOGO BMW ==========")

imagen_bmw = cv2.imread("BMW.jpg")

if imagen_bmw is None:

    print("Error: no se encontró el archivo BMW.jpg")

else:

    # Convertir a escala de grises
    gris_bmw = cv2.cvtColor(
        imagen_bmw,
        cv2.COLOR_BGR2GRAY
    )

    # Detectar bordes
    bordes_bmw = cv2.Canny(
        gris_bmw,
        50,
        150
    )

    # Obtener contornos
    contornos_bmw, _ = cv2.findContours(
        bordes_bmw,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_NONE
    )

    print("\nCoordenadas de los contornos BMW:")

    contador = 0

    for contorno in contornos_bmw:

        puntos = contorno[:, 0, :]

        x = puntos[:, 0]

        y = -puntos[:, 1]

        # Evitar el borde exterior de toda la imagen
        if (
            np.max(x) - np.min(x)
            < imagen_bmw.shape[1] * 0.95
            and
            np.max(-y) - np.min(-y)
            < imagen_bmw.shape[0] * 0.95
        ):

            print(
                f"\nContorno BMW {contador + 1}"
            )

            

            contador += 1


    # Graficar
    plt.figure(
        figsize=(8, 8)
    )

    for contorno in contornos_bmw:

        puntos = contorno[:, 0, :]

        x = puntos[:, 0]

        y = -puntos[:, 1]

        if (
            np.max(x) - np.min(x)
            < imagen_bmw.shape[1] * 0.95
            and
            np.max(-y) - np.min(-y)
            < imagen_bmw.shape[0] * 0.95
        ):

            plt.plot(
                x,
                y
            )

    plt.title(
        "Contornos del logo BMW"
    )

    plt.xlabel("X")

    plt.ylabel("Y")

    plt.axis("equal")

    plt.grid(True)

    plt.show()
