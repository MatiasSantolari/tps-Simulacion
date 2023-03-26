import random;
import math
import matplotlib.pyplot as plt

#genero una lista de 100 numeros aleatorios entre 0 y 38
def cargarListaNros(nrosPorTirada):
    listaNros = [];
    b = 0;
    for i in range(0, nrosPorTirada):
        b = random.randint(0, 38);
        listaNros.append(b);
    return listaNros
#promedio = suma de todos los elementos de la muestra dividido dicha cantidad de elementos
def cargarPromedio(listaNros, nrosPorTirada):
    suma = sum(listaNros)
    promedio = suma/nrosPorTirada
    return promedio
#varianza mide que tan lejos está la muestra de lo que dió el promedio de dicha muestra
def cargarVarianza(listaNros, promedio, nrosPorTirada):
    sumatoria = 0
    for i in range(0, nrosPorTirada):
        sumatoria = sumatoria + (listaNros[i]-promedio)
    varianzaAlCuadrado = (sumatoria ** 2)/(nrosPorTirada - 1)
    varianza = math.sqrt(varianzaAlCuadrado)
    return varianza
#desvio estandar = raiz cuadrada de la varianza
def cargarDesvio(varianza):
    desvio = math.sqrt(varianza)
    return desvio

def frecuenciaRelativa(listaNros, a):
    fa = listaNros.count(a)
    fr = fa / nrosPorTirada
    return fr

def graficar_estadisticas(listaPromedios, listaVarianzas, listaDesvios, listaFrecuencias):
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    axs[0, 0].plot(listaPromedios)
    axs[0, 0].set_title('Promedios')

    axs[0, 1].plot(listaVarianzas)
    axs[0, 1].set_title('Varianzas')

    axs[1, 0].plot(listaDesvios)
    axs[1, 0].set_title('Desvíos')

    axs[1, 1].plot(listaPromedios, color='blue', label='Promedios')
    axs[1, 1].plot(listaVarianzas, color='orange', label='Varianzas')
    axs[1, 1].plot(listaDesvios, color='green', label='Desvíos')
    axs[1, 1].plot(listaFrecuencias, color='red', label='Frecuencias Relativas')
    axs[1, 1].legend(loc='upper left')
    axs[1, 1].set_title('Promedios,Varianzas,Desvios,Frecuencias Relativas')

    plt.show()

    plt.plot(listaFrecuencias)
    plt.legend()
    plt.show()

cantNrosRuleta = 39
nrosPorTirada = 100
listaNros, promedio, varianza, desvio = [], [], [], []
listasNros, promedios, frecuencias, varianzas, desvios  = [], [], [], [], []
"""la listaNros es una lista que contiene los 100 nros que hayan salido en la tirada actuali
    mientras que listasNros contiene todas las listaNros"""

a = random.randint(0, 38)

for i in range(0,25):
    listaNros = cargarListaNros(nrosPorTirada)

    promedio = cargarPromedio(listaNros, nrosPorTirada)
    promedios.append(promedio)

    varianza = cargarVarianza(listaNros, promedio, nrosPorTirada)
    varianzas.append(varianza)

    desvio = cargarDesvio(varianza)
    desvios.append(desvio)

    fr = frecuenciaRelativa(listaNros,a)
    frecuencias.append(fr)

print("promedios: ", promedios)
print("varianzas: ", varianzas)
print("desvios: ", desvios)
print("frecuencias: ", frecuencias)

graficar_estadisticas(promedios,varianzas,desvios,frecuencias)



