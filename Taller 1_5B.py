#5B. ¿Desea continuar?

respuesta = ""

while respuesta.lower() != "no":

    respuesta = input("¿Desea continuar? (Si/No): ")

    if respuesta.lower() == "si":
        print("El programa continúa.\n")

    elif respuesta.lower() == "no":
        print("El programa ha terminado.")

    else:
        print("Respuesta no válida. Escriba Si o No.\n")
