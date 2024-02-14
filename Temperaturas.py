import random

def llenarLista():
    return [random.uniform(15, 30) for _ in range(30)]

def calcularMitad1(temperaturas):
    return sum(temperaturas[:15]) / 15

def calcularMitad2(temperaturas):
    return sum(temperaturas[15:]) / 15

def calcularTercio(temperaturas, tercio):
    inicio = int(len(temperaturas) * (tercio - 1) / 3)
    fin = int(len(temperaturas) * tercio / 3)
    return sum(temperaturas[inicio:fin]) / (fin - inicio)

temperaturas_mes = llenarLista()

promedio_mitad1 = calcularMitad1(temperaturas_mes)
promedio_mitad2 = calcularMitad2(temperaturas_mes)

promedio_tercio1 = calcularTercio(temperaturas_mes, 1)
promedio_tercio2 = calcularTercio(temperaturas_mes, 2)
promedio_tercio3 = calcularTercio(temperaturas_mes, 3)

print("Temperaturas del mes:", temperaturas_mes)
print("Promedio primera mitad del mes:", promedio_mitad1)
print("Promedio segunda mitad del mes:", promedio_mitad2)
print("Promedio primer tercio del mes:", promedio_tercio1)
print("Promedio segundo tercio del mes:", promedio_tercio2)
print("Promedio tercer tercio del mes:", promedio_tercio3)
