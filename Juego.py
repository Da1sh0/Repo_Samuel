import random

def juego():
    numero_correcto = random.randint(1, 10)
    intentos_restantes = 5

    while intentos_restantes > 0:
        intento = input("Adivina el número (entre 1 y 10): ")

        try:
            intento = int(intento)
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if 1 <= intento <= 10:
            if intento == numero_correcto:
                print("¡Felicidades, adivinaste el número!")
                break
            elif intento < numero_correcto:
                intentos_restantes -= 1
                print("El número es mayor.")
                print("Incorrecto. Te quedan", intentos_restantes, "intentos.")
            else:
                intentos_restantes -= 1
                print("El número es menor.")
                print("Incorrecto. Te quedan", intentos_restantes, "intentos.")
        else:
            print("Por favor, ingresa un número entre 1 y 10.")

    if intentos_restantes == 0:
        print("Lo siento, te quedaste sin intentos. El número correcto era", numero_correcto)

juego()


#Diiego