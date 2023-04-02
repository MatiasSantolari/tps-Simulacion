import random
import matplotlib.pyplot as plt
import numpy as np

#genero una lista de 100 numeros aleatorios entre 0 y 38
def cargarListaNros(nrosPorTirada):
    listaNros = []
    b = 0
    for i in range(0, nrosPorTirada):
        b = random.randint(0, 36)
        listaNros.append(b)
    return listaNros
#promedio = suma de todos los elementos de la muestra dividido dicha cantidad de elementos
def cargarPromedio(listaNros, nrosPorTirada):
    suma = sum(listaNros)
    promedio = suma/nrosPorTirada
    return promedio
#varianza mide que tan lejos está la muestra de lo que dió el promedio de dicha muestra
def cargarVarianza(listaNros):
    varianza = np.var(listaNros)
    return varianza
#desvio estandar = raiz cuadrada de la varianza
def cargarDesvio(listaNros):
    desvio = np.std(listaNros)
    return desvio
def frecuenciaRelativa(listaNros, a):
    fa = listaNros.count(a)
    fr = fa / nrosPorTirada
    return fr
def graficar_estadisticas(listaPromedios, listaVarianzas, listaDesvios, listaFrecuencias, frecuenciaEsperada):
    #graficar promedios
    plt.plot(listaPromedios)
    plt.axhline(37 / 2, color='r', linestyle='-', label="vpe valor promedio esperado")
    plt.legend()
    plt.xlabel("n (número de tiradas)")
    plt.ylabel("vp valor promedio de las tiradas")
    plt.title('Promedio en 200 tiradas de 100 jugadas')
    plt.show()
    #graficar varianzas
    plt.plot(listaVarianzas)
    plt.xlabel("n (número de tiradas)")
    plt.ylabel("v varianza de cada una de las tiradas")
    plt.title('Varianza en 200 tiradas de 100 jugadas')
    plt.show()
    #graficar desvios
    plt.plot(listaDesvios)
    plt.xlabel("n (número de tiradas)")
    plt.ylabel("d desvio de cada una de las tiradas")
    plt.title('Desvio en 200 jugadas de 100 tiradas')
    plt.show()
    #graficar frecuencias
    plt.plot(listaFrecuencias)
    plt.axhline(frecuenciaEsperada, color='r', linestyle='-', label="fe frecuencia esperada")
    plt.legend()
    plt.xlabel("n (número de tiradas)")
    plt.ylabel("f frec. relativa de cada una de las tiradas")
    plt.title('Frec. relativa en 200 jugadas de 100 tiradas')
    plt.show()

def main(nrosPorTirada,a):
    listasNros, promedios, frecuencias, varianzas, desvios = [], [], [], [], []

    for i in range(0, 200):
        listaNros = cargarListaNros(nrosPorTirada)

        promedio = cargarPromedio(listaNros, nrosPorTirada)
        promedios.append(promedio)

        varianza = cargarVarianza(listaNros)
        varianzas.append(varianza)

        desvio = cargarDesvio(listaNros)
        desvios.append(desvio)

        fr = frecuenciaRelativa(listaNros, a)
        frecuencias.append(fr)

    return listasNros, promedios, frecuencias, varianzas, desvios
################################################################################################
cantNrosRuleta = 37
nrosPorTirada = 100
frecuenciaEsperada = 1/cantNrosRuleta
a = random.randint(0, cantNrosRuleta - 1) #elijo un numero al azar

listasNros, promedios, frecuencias, varianzas, desvios = [], [], [], [], []
listasNros, promedios, frecuencias, varianzas, desvios = main(nrosPorTirada,a)
graficar_estadisticas(promedios, varianzas, desvios, frecuencias, frecuenciaEsperada)

familiaPromedios,familiaFrecuencia, familiaVarianzas,familiaDesvios = [],[],[],[]

for j in range(3):
    listasNros, promedios, frecuencias, varianzas, desvios = main(nrosPorTirada, a)
    familiaPromedios.append(promedios)
    familiaFrecuencia.append(frecuencias)
    familiaVarianzas.append(varianzas)
    familiaDesvios.append(desvios)

#graficar promedios
for k in range(3):
    plt.plot(familiaPromedios[k])
plt.axhline(37 / 2, color='r', linestyle='-', label="vpe valor promedio esperado")
plt.legend()
plt.xlabel("n (número de tiradas)")
plt.ylabel("vp valor promedio de las tiradas")
plt.title('Promedio en 200 tiradas de 100 jugadas x 3')
plt.show()
#graficar varianzas
for k in range(3):
    plt.plot(familiaVarianzas[k])
plt.xlabel("n (número de tiradas)")
plt.ylabel("v varianza de cada una de las tiradas")
plt.title('Varianza en 200 tiradas de 100 jugadas x 3')
plt.show()
#graficar desvios
for k in range(3):
    plt.plot(familiaDesvios[k])
plt.xlabel("n (número de tiradas)")
plt.ylabel("d desvio de cada una de las tiradas")
plt.title('Desvio en 200 jugadas de 100 tiradas x 3')
plt.show()
#graficar frecuencias
for k in range(3):
    plt.plot(familiaFrecuencia[k])
plt.axhline(frecuenciaEsperada, color='r', linestyle='-', label="fe frecuencia esperada")
plt.legend()
plt.xlabel("n (número de tiradas)")
plt.ylabel("f frec. relativa de cada una de las tiradas")
plt.title('Frec. relativa en 200 jugadas de 100 tiradas x 3')
plt.show()





