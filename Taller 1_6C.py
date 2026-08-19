# C6 - CONTORNOS DE DOS LOGOS DE AUTOMÓVILES
# Mazda y BMW

import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files


# 1. SUBIR LAS IMÁGENES


print("Seleccione las imágenes de Mazda y BMW:")
uploaded = files.upload()


# Buscar automáticamente los archivos
archivo_mazda = None
archivo_bmw = None

for nombre in uploaded.keys():

    nombre_minuscula = nombre.lower()

    if "mazda" in nombre_minuscula:
        archivo_mazda = nombre

    elif "bmw" in nombre_minuscula:
        archivo_bmw = nombre


print("\nArchivos encontrados:")
print("Mazda:", archivo_mazda)
print("BMW:", archivo_bmw)


# ============================================================
# 2. LOGO MAZDA
# ============================================================

if archivo_mazda is not None:

    imagen_mazda = cv2.imread(archivo_mazda)

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

    # Dilatar ligeramente los bordes
    kernel = np.ones((3, 3), np.uint8)

    bordes_mazda = cv2.dilate(
        bordes_mazda,
        kernel,
        iterations=1
    )

    # Buscar contornos
    contornos_mazda, _ = cv2.findContours(
        bordes_mazda,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_NONE
    )

    # Ordenar contornos por área
    contornos_mazda = sorted(
        contornos_mazda,
        key=cv2.contourArea,
        reverse=True
    )

    # Quedarnos con los contornos grandes
    contornos_mazda = [
        c for c in contornos_mazda
        if cv2.contourArea(c) > 1000
    ]

    # Mostrar contornos
    plt.figure(figsize=(10, 6))

    for contorno in contornos_mazda[:10]:

        puntos = contorno[:, 0, :]

        x = puntos[:, 0]
        y = -puntos[:, 1]

        plt.plot(x, y)

    plt.title("Contornos del logo Mazda")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.axis("equal")
    plt.grid(True)

    plt.show()


else:

    print("No se encontró la imagen de Mazda.")


# ============================================================
# 3. LOGO BMW
# ============================================================

if archivo_bmw is not None:

    imagen_bmw = cv2.imread(archivo_bmw)

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

    # Buscar contornos
    contornos_bmw, _ = cv2.findContours(
        bordes_bmw,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_NONE
    )

    # Crear gráfica
    plt.figure(figsize=(8, 8))

    for contorno in contornos_bmw:

        puntos = contorno[:, 0, :]

        x = puntos[:, 0]
        y = -puntos[:, 1]

        # Evitar solamente los contornos que corresponden
        # al borde exterior de toda la imagen
        if (
            np.max(x) - np.min(x) < imagen_bmw.shape[1] * 0.95
            and
            np.max(-y) - np.min(-y) < imagen_bmw.shape[0] * 0.95
        ):

            plt.plot(x, y)

    plt.title("Contornos del logo BMW")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.axis("equal")
    plt.grid(True)

    plt.show()

else:

    print("No se encontró la imagen de BMW.")

# ============================================================
# 4. FINAL
# ============================================================

print("\n========================================")
print("PROCESAMIENTO TERMINADO")
print("Se obtuvieron coordenadas X e Y")
print("de los contornos de Mazda y BMW.")
print("========================================")
