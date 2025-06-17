import random
import os

def jugar():
    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100...")

    archivo_record = "record.txt"

    # Crear archivo si no existe
    if not os.path.exists(archivo_record):
        with open(archivo_record, "w") as f:
            f.write("9999")

    # Leer récord
    with open(archivo_record, "r") as f:
        record = int(f.read())

    numero_secreto = random.randint(1, 100)
    intentos = 0
    limite_intentos = 7

    while intentos < limite_intentos:
        intento = input("Adivina el número: ")

        if not intento.isdigit():
            print("Por favor, ingresa un número válido.")
            continue

        intento = int(intento)
        intentos += 1

        if intento < numero_secreto:
            print("Muy bajo ⬇")
        elif intento > numero_secreto:
            print("Muy alto ⬆")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos 🎉")

            if intentos < record:
                print("¡Nuevo récord!")
                with open(archivo_record, "w") as f:
                    f.write(str(intentos))
            else:
                print(f"El récord actual es {record} intentos. ¡Intenta superarlo!")
            break
    else:
        print(f"Demasiados intentos crac, el número era {numero_secreto}")

# 🔁 Bucle de reinicio
while True:
    jugar()
    respuesta = input("¿Quieres jugar de nuevo? (si/no): ").lower()
    if respuesta != "si":
        print("¡Gracias por jugar! 👋")
        break