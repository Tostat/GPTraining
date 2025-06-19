import random
import os

print("Resuelva las siguientes multiplicaciones:")
rec = "rec.txt"
racha = 0

# Si no existe el archivo, lo crea con 0
if not os.path.exists(rec):
    with open(rec, "w") as f:
        f.write("0")

# Lee el récord actual
with open(rec, "r") as f:
    record = int(f.read())

while True:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    resp = input(f"{num1} x {num2} = ")
    rcor = num1 * num2

    try:
        x = int(resp)
    except ValueError:
        print("Eso no es un número")
        continue

    if x == rcor:
        racha += 1
        otra = input("¡Correcto! ¿Quieres otra? (si/no): ").lower()
        if otra != "si":
            if racha > record:
                print(f"¡Nuevo récord! Has hecho {racha} seguidas!")
                with open(rec, "w") as f:
                    f.write(str(racha))
            else:
                print(f"Tu racha fue {racha}. El récord es {record}.")
            print("Gracias por jugar!")
            break
    else:
        print(f"Incorrecto, daba {rcor}.")
        if racha > record:
            print(f"Sin embargo tu racha fue {racha}! Nuevo récord!")
        else:
            print(f"Tu racha fue {racha}")
        racha = 0
