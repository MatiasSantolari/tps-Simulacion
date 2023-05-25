# TEST
import numpy as np
import scipy.stats as sp
import math

import matplotlib.pyplot as plt


def testKS(datos, alfa):
    print("Prueba de Frecuencias - Prueba de Kolmogorov-Smirnov")
    datos = np.sort(datos)
    n = np.size(datos)
    d1 = []
    d2 = []
    for i in range(n):
        aux = (i + 1) / n
        d1.insert(i, round(aux - datos[i], 4))
        d2.insert(i, round(datos[i] - (i / n), 4))
    d = max(np.amax(d1), np.amax(d2))
    valorCritico = sp.ksone.ppf(1 - alfa / 2, n)
    print("Valor estadístico D = " + str(d))
    print(
        "El valor estadístico de la tabla (cuyo nivel de significancia es α = "
        + str(alfa)
        + ") es Dα = "
        + str(valorCritico)
    )
    if valorCritico >= d:
        print(
            "Aceptación de Ho: NO hay evidencia suficiente para rechazar la hipotesis (D < Dα)"
        )
    else:
        print(
            "Rechazo de Ho: HAY evidencia suficiente para rechazar la hipotesis (D > Dα)"
        )


def testChiCuadrada(datos, alfa):
    print("Prueba de Frecuencias - Prueba Chi-Cuadrada")
    n = np.size(datos)
    m = 10  # nro de Intervalos, cada uno de longitud 0.1
    esperados = [n / m, n / m, n / m, n / m, n / m, n / m, n / m, n / m, n / m, n / m]
    observados = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(n):
        if datos[i] <= 0.1:
            observados[0] += 1
        elif datos[i] <= 0.2:
            observados[1] += 1
        elif datos[i] <= 0.3:
            observados[2] += 1
        elif datos[i] <= 0.4:
            observados[3] += 1
        elif datos[i] <= 0.5:
            observados[4] += 1
        elif datos[i] <= 0.6:
            observados[5] += 1
        elif datos[i] <= 0.7:
            observados[6] += 1
        elif datos[i] <= 0.8:
            observados[7] += 1
        elif datos[i] <= 0.9:
            observados[8] += 1
        elif datos[i] <= 1.0:
            observados[9] += 1
    f = []
    for i in range(m):
        f.insert(i, pow(observados[i] - esperados[i], 2) / esperados[i])
    estadistico = np.sum(f)
    valorCritico = sp.chi2.ppf(1 - alfa, m - 1)
    print("El valor estadístico es X² = " + str(estadistico))
    print(
        "El valor estadístico de la tabla (con nivel de significancia α = "
        + str(alfa)
        + ") es X²α = "
        + str(valorCritico)
    )
    if valorCritico >= estadistico:
        print(
            "Aceptación de Ho: NO hay suficiente evidencia para rechazar la hipotesis (X² < X²α)"
        )
    else:
        print(
            "Rechazo de Ho: HAY suficiente evidencia para rechazar la hipotesis (X² > X²α)"
        )


def testPoker(datos, alfa):
    print("Prueba de Póker")
    n = np.size(datos)
    freqEsp = [
        n * 0.3024,
        n * 0.504,
        n * 0.108,
        n * 0.072,
        n * 0.009,
        n * 0.0045,
        n * 0.0001,
    ]
    # freqEsp=[Diferentes,Un Par, DosPares, Tercia,  Full,    Poker,    Quintilla]
    freqObs = [0, 0, 0, 0, 0, 0, 0]
    for i in range(n):
        lista = []
        for j in str(format(datos[i], ".5f"))[
            1:
        ]:  # tomo los primeros 5 decimales de cada numero
            if j.isdigit():
                lista.append(j)
        # analizo cada decimal (u) y la cantidad de veces que aparece (veces)
        u, veces = np.unique(lista, return_counts=True)
        if np.amax(veces) == 5:  # [6]: Quintilla
            freqObs[6] += 1
        elif np.amax(veces) == 4:  # [5]: Poker
            freqObs[5] += 1
        elif np.amax(veces) == 3:
            if np.size(veces) == 2:  # [4]: Full
                freqObs[4] += 1
            else:  # [3]: Tercia
                freqObs[3] += 1
        elif np.amax(veces) == 2:
            if np.size(veces) == 3:  # [2]: Dos Pares
                freqObs[2] += 1
            else:  # [1]: Un Par
                freqObs[1] += 1
        else:  # [0]: Diferentes
            freqObs[0] += 1
    fe = []
    fo = []
    j = -1
    for i in range(np.size(freqEsp)):
        if freqEsp[i] >= 5:
            fe.append(freqEsp[i])
            fo.append(freqObs[i])
            j += 1
        else:
            # guardo las frecuencias esperadas pequeñas en un mismo intervalo
            fe[j] += freqEsp[i]
            fo[j] += freqObs[i]
    f = []
    m = np.size(fe)  # nro de intervalos
    for i in range(m):
        f.append((fe[i] - fo[i]) ** 2 / fe[i])
    estadistico = np.sum(f)  # calculo el estadistico de prueba
    # Si "estadistico" es mayor al valor establecido en la tabla, dado un intervalo de confianza (q) y grados de libertad (df) -> entonces no cumple
    valorCritico = sp.chi2.ppf(
        q=1 - alfa, df=m - 1
    )  # calcula el estadistico de chi-cuadrado
    print("El valor estadístico es X² = " + str(estadistico))
    print(
        "El valor estadístico de la tabla (con nivel de significancia α = "
        + str(alfa)
        + ") es X²α = "
        + str(valorCritico)
    )
    if valorCritico >= estadistico:
        print(
            "Aceptación de Ho: NO hay suficiente evidencia para rechazar la hipotesis (X² < X²α)"
        )
    else:
        print(
            "Rechazo de Ho: HAY suficiente evidencia para rechazar la hipotesis (X² > X²α)"
        )


def testCorridas(datos, alfa):
    print("Prueba de corridas - Arriba y abajo de la media para numeros uniformes")
    media = np.mean(datos)
    # agrego 1 si el valor está encima de la media y 0 si está por debajo
    sec = [1 if r > media else 0 for r in datos]
    n = np.size(datos)
    corridas = 0
    for i in range(0, len(sec) - 1):
        # calculo las veces que cambian los valores consecutivos, es decir se cortan la racha
        if sec[i] != sec[i + 1]:
            corridas += 1
    x0 = sec.count(0)  # cantidad de ceros
    x1 = sec.count(1)  # cantidad de unos
    mediaC = ((2 * x0 * x1) / (x0 + x1)) + 1
    varianzaC = ((2 * x0 * x1) * (2 * x0 * x1 - n)) / ((n**2) * (n - 1))
    desvioC = math.sqrt(varianzaC)
    print(
        f"Datos de la prueba: Media = {mediaC} - Varianza = {varianzaC} - Corridas = {corridas}"
    )
    z = abs((corridas - mediaC) / desvioC)
    print(f"El Valor estadistico de prueba es Z = {z}")
    Ztabla = sp.norm.ppf(1 - alfa / 2)
    print(
        f"El Valor estadistico de tabla (nivel de significacia α={alfa}) es Zα = {Ztabla}"
    )
    # si el estadistico observado es mayor al estadistico de tabla la prueba se rechaza
    if z < Ztabla:
        print("Aceptación de Ho: La hipotesis no puede ser rechazada  (Z < Zα)")
    if z > Ztabla:
        print(
            "Rechazo de Ho: La secuencia de números NO es independiente y por lo tanto la secuencia NO es aleatoria. (Z > Zα)"
        )
