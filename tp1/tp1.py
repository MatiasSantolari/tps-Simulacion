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

cantNrosRuleta = 39
nrosPorTirada = 100
listaNros, promedio, varianza, desvio = [], [], [], []
listasNros, promedios, frecuencias, varianzas, desvios  = [], [], [], [], []
"""la listaNros es una lista que contiene los 100 nros que hayan salido en la tirada actuali
    mientras que listasNros contiene todas las listaNros"""

listaNros = cargarListaNros(nrosPorTirada)
promedio = cargarPromedio(listaNros, nrosPorTirada)
promedios.append(promedio)
varianza = cargarVarianza(listaNros,promedio,nrosPorTirada)
varianzas.append(varianza)
desvio = cargarDesvio(varianza)
desvios.append(desvio)


# Lista de 10 varianzas
variances = [1.2, 2.5, 3.1, 0.9, 1.6, 2.3, 1.8, 2.7, 3.2, 1.5]

# Creamos una lista de números del 0 al 9 para etiquetar las barras
indices = range(len(variances))

# Creamos el gráfico de barras utilizando la función bar de matplotlib
plt.bar(indices, variances)

# Añadimos las etiquetas del eje x con la función xticks de matplotlib
plt.xticks(indices, indices)

# Mostramos el gráfico
plt.show()
