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





# Definir una lista de desviaciones estándar
desviaciones = [1.5, 2.1, 0.8, 1.9, 1.1, 1.6, 2.3, 1.7, 2.2, 2.0]

# Calcular el promedio de las desviaciones
promedio = sum(desviaciones) / len(desviaciones)

# Crear una lista de valores x para los puntos de la función lineal
x = list(range(len(desviaciones)))

# Crear una lista de valores y para los puntos de la función lineal
y = [promedio] * len(desviaciones)

# Crear el gráfico
plt.plot(x, desviaciones, label='Desviaciones')
plt.plot(x, y, label='Promedio')

# Configurar el gráfico
plt.title('Desviaciones estándar')
plt.xlabel('Índice')
plt.ylabel('Desviación estándar')
plt.legend()

# Mostrar el gráfico
plt.show()
