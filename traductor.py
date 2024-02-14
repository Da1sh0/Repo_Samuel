def traducir(palabra):
    traduccion = {
        "rojo": "red",
        "azul": "blue",
        "verde": "green",
        "amarillo": "yellow",
        "naranja": "orange",
        "morado": "purple",
        "rosado": "pink",
        "negro": "black",
        "blanco": "white",
        "gris": "gray",
    }

    palabra_minusculas = palabra.lower()

    if palabra_minusculas in traduccion:
        return traduccion.get(palabra_minusculas), 'espanol'
    else:
        traduccion_inversa = {v: k for k, v in traduccion.items()}
        return traduccion_inversa.get(palabra_minusculas), 'ingles'

color = input("Ingrese un color en español o inglés, en mayúsculas o minúsculas: ")

resultado, idioma = traducir(color)
if resultado:
    print("La traducción de ",color," es ",resultado,".")
else:
    print("No se pudo determinar la traducción. Verifique la palabra ingresada.")
