import matplotlib.pyplot as plt
import numpy as np

def calcular_estadisticas(datos):
    listaPromedios = []
    listaVarianzas = []
    listaDesvios = []

    for lista in datos:
        promedio = np.mean(lista)
        varianza = np.var(lista)
        desvio = np.std(lista)
        listaPromedios.append(promedio)
        listaVarianzas.append(varianza)
        listaDesvios.append(desvio)

    return listaPromedios, listaVarianzas, listaDesvios

def graficar_estadisticas(listaPromedios, listaVarianzas, listaDesvios):
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    axs[0, 0].plot(listaPromedios)
    axs[0, 0].set_title('Promedios')

    axs[0, 1].plot(listaVarianzas)
    axs[0, 1].set_title('Varianzas')

    axs[1, 0].plot(listaDesvios)
    axs[1, 0].set_title('Desvíos')

    axs[1, 1].plot(listaPromedios, label='Promedios')
    axs[1, 1].plot(listaVarianzas, label='Varianzas')
    axs[1, 1].plot(listaDesvios, label='Desvíos')
    axs[1, 1].legend(loc='upper left')
    axs[1, 1].set_title('Todas las estadísticas')

    plt.show()


datos = [
    [1, 0, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [6, 35, 15],
    [6, 17, 2],
    [19, 20, 21],
    [12, 23, 24],
    [4, 26, 7],
    [28, 2, 30]
]

listaP,listaV,listaD = [],[],[]
listaP,listaV,listaD = calcular_estadisticas(datos)
graficar_estadisticas(listaP,listaV,listaD)


