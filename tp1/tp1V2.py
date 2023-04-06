import matplotlib.pyplot as plt
import random
import numpy as np


def genera_lista_muestras(cantidad_numeros_aleatorios, rango_desde, rango_hasta):
    lista = []
    for i in range(cantidad_numeros_aleatorios):
        numero_aleatorio = random.randint(rango_desde, rango_hasta)
        lista.append(numero_aleatorio)
    return lista

#frecuencia relativa de cada uno de los numeros del plato de la ruleta
def frecuencia_relativa(lista, rango_hasta):
    lista_frecuencias_relativas = []
    for i in range(rango_hasta):
        lista_frecuencias_relativas.append(lista.count(i) / len(lista))
    return lista_frecuencias_relativas

def frecuencia_relativa_nro_elegido(nroElegido, lista):
    listaFrec = []
    for i in range(len(lista)):
        a = lista[:i + 1].count(nroElegido)
        fr = a/len(lista[:i + 1])
        listaFrec.append(fr)
    return listaFrec


def dibujar_media(lista):
    lista_promedios_ejecucion_x = []
    for i in range(cantidad_numeros_aleatorios):
        lista_promedios_ejecucion_x.append(np.mean(lista[:i + 1]))
    plt.plot(lista_promedios_ejecucion_x)


def dibujar_varianza(lista):
    lista_varianza_ejecucion_x = []
    for i in range(cantidad_numeros_aleatorios):
        lista_varianza_ejecucion_x.append(np.var(lista[:i + 1]))
    plt.plot(lista_varianza_ejecucion_x)


def dibujar_desvio_estandar(lista):
    desvio_estandar_ejecucion_x = []
    for i in range(cantidad_numeros_aleatorios):
        desvio_estandar_ejecucion_x.append(np.std(lista[:i + 1]))
    plt.plot(desvio_estandar_ejecucion_x)

def dibujar_frecuencia_relativa(nroElegido,lista):
    plt.plot(frecuencia_relativa_nro_elegido(nroElegido, lista))

#################Inicio
print("Numeros aleatorios")
cantidad_numeros_aleatorios = 5000
## Espacio muestral [0..36]
rango_desde = 0
rango_hasta = 36
promedio = 0

lista = []
lista_promedios_muestra_n = []
lista_desvio_estandar = []
lista_varianza = []
suma = 0

nroElegido = random.randint(0,36)

matriz_muestras = []

for i in range(5):
    matriz_muestras.append(genera_lista_muestras(cantidad_numeros_aleatorios, rango_desde, rango_hasta))

for i in range(len(matriz_muestras)):
    dibujar_media(matriz_muestras[i])

plt.axhline(rango_hasta / 2, color='r', linestyle='-', label="vpe valor promedio esperado")
plt.legend()
plt.xlabel("n (número de tiradas)")
plt.ylabel("vp valor promedio de las tiradas")
plt.title('Promedio en 5 jugadas de 5000 tiradas')
plt.show()

for i in range(len(matriz_muestras)):
    dibujar_varianza(matriz_muestras[i])
# plt.axhline([valor], color='r', linestyle='-', label = "vve valor de la varianza esperada")
plt.legend()
plt.xlabel("n (número de tiradas)")
plt.ylabel("vv valor de la varianza")
plt.title('Varianza en 5 jugadas de 5000 tiradas')
plt.show()

for i in range(len(matriz_muestras)):
    dibujar_desvio_estandar(matriz_muestras[i])
# plt.axhline([valor], color='r', linestyle='-', label = "vve valor de la varianza esperada")
plt.legend()
plt.xlabel("n (número de tiradas)")
plt.ylabel("vd valor del desvío")
plt.title('Desvio en 5 jugadas de 5000 tiradas')
plt.show()

x1 = []
for i in range(rango_hasta + 1):
    x1.append(i)

frecuencia_esperada = 1 / (rango_hasta + 1)
print("Frecuencia relativa esperada")
print(frecuencia_esperada)
lista_frecuencias = frecuencia_relativa(matriz_muestras[1], rango_hasta + 1)
plt.ylim(0, 0.1)
plt.axhline(frecuencia_esperada, color='g', linestyle='-', label="Frecuencia esperada")
plt.legend()
plt.bar(x1, lista_frecuencias)
plt.ylabel('Frecuencia relativa')
plt.xlabel('Valores posibles')
plt.title('Frecuencias relativas')
plt.show()

#frecuencia relativa de un numero elegido aleatoriamente
dibujar_frecuencia_relativa(nroElegido,matriz_muestras[1])
plt.axhline(frecuencia_esperada, color='g', linestyle='-', label="Frecuencia esperada")
plt.legend()
plt.ylabel('Frecuencia relativa')
plt.xlabel("n (número de tiradas)")
plt.title('Frecuencia relativas con respecto a un numero elegido')
plt.show()


#lo mismo que antes pero con x5
for i in range(len(matriz_muestras)):
    dibujar_frecuencia_relativa(nroElegido,matriz_muestras[i])
plt.axhline(frecuencia_esperada, color='g', linestyle='-', label="Frecuencia esperada")
plt.legend()
plt.ylabel('Frecuencia relativa')
plt.xlabel("n (número de tiradas)")
plt.title('5 Frecuencias relativas con respecto a un numero elegido')
plt.show()
