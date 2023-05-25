import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as sp
from scipy.stats import (
    gamma as gam,
    norm,
    nbinom,
    binom,
    poisson,
    hypergeom,
    uniform,
    expon,
    geom,
    kstest,
    probplot,
)
from math import sqrt, pi, exp, gamma, factorial, trunc, comb


def test_prob_param(lista_binom, n, p):
    k = 17
    prob = binom.pmf(k, n, p)
    print("Probabilidad de obtener {} éxitos: {:.4f}".format(k, prob))
    print(
        "Probabilidad de obtener {} éxitos en muestra: {:.4f}".format(
            k, np.mean(np.array(lista_binom) == k)
        )
    )

    # Calcular la función de distribución acumulativa (FDA) hasta k éxitos
    cum_prob = binom.cdf(k, n, p)
    print("Probabilidad de obtener {} o menos éxitos: {:.4f}".format(k, cum_prob))
    print(
        "Probabilidad de obtener {} o menos éxitos en muestra: {:.4f}".format(
            k, np.mean(np.array(lista_binom) <= k)
        )
    )

    # Calcular el valor esperado (media) y varianza
    mean = binom.mean(n, p)
    variance = binom.var(n, p)
    print("Media: {:.2f}".format(mean))
    print("Media muestral: {:.2f}".format(np.mean(lista_binom)))
    print("Varianza: {:.2f}".format(variance))
    print("Varianza muestral: {:.2f}".format(np.var(lista_binom)))


def test_qq(hypergeom_sample, N, n, p, axes, place):
    # Crear el gráfico Q-Q
    _, r = probplot(
        hypergeom_sample, dist=hypergeom, sparams=(N, n, N * p), plot=axes[place]
    )

    # Imprimir el coeficiente de correlación
    print("Coeficiente de correlación:", r)

    # Mostrar el gráfico
    axs[place].set_title("Gráfico Q-Q")


# Test basado en los momentos para poisson
def u_statistic(sample):
    n = len(sample)
    mean = np.mean(sample)
    sc = np.sum((sample - mean) ** 2) / (n - 1)
    D = sc / mean

    return D


def KolmogorovTest(lista, alfa, dist_name, params):
    """Test de Kolmogorov-Smirnov, compara el cdf(valor crítico) de una distribucion
    con el cdf(d) de la muestra(lista) de tamaño n, para el nivel de significancia alfa.
    Devuelve verdadero si la distribución es uniforme, falso si no lo es."""

    distributions = {
        "uniform": "uniform",
        "expon": "expon",
        "gam": "gamma",
        "norm": "norm",
        "nbinom": "nbinom",
        "binom": "binom",
        "hypergeom": "hypergeom",
        "poisson": "poisson",
    }

    dist = distributions[dist_name]
    if dist_name == "uniform":
        ks_statistic, p_value = kstest(lista, "uniform", args=(5, 15))
    elif dist_name == "poisson":
        d = u_statistic(lista)
        if d > 0.95 and d < 1.05:
            return f"Pasa prueba. {d} ≈ 1"
        else:
            return f"No pasa prueba. {d} lejado a 1"
    else:
        ks_statistic, p_value = kstest(lista, dist, args=params)

    print("Distribución:", dist_name)

    if alfa < p_value:
        # Hipótesis aceptada, distribución es uniforme
        return f"Pasa prueba {alfa} < {p_value}"
    # Hipótesis rechazada, distribución no es uniforme
    return f"No pasa prueba {alfa} > {p_value}"


# --------------------------------UNIFORME-M-RECHAZO-------------------------------------


def densidad_uniforme(x, a, b):
    if a <= x <= b:
        return 1 / (b - a)
    else:
        return 0


def uniformeR(a, b, c, pseudos, n):
    aceptados = []
    for r1 in pseudos:
        while len(aceptados) < n:
            r2 = np.random.uniform(0, 1)
            x = a + (b - a) * r1
            if r2 <= c * densidad_uniforme(x, a, b):
                aceptados.append(x)
                break

    return aceptados


n = 10000
a, b = 5, 20
c = 1 / densidad_uniforme((b + a) / 2, a, b)
total = []
fig, axs = plt.subplots(ncols=2, nrows=1, constrained_layout=True, figsize=[7.5, 4])
for rep in range(30):
    lista_r = [random.random() for _ in range(n)]
    lista_x = uniformeR(a, b, c, lista_r, n)
    total.extend(lista_x)
    if rep == 1:
        axs[0].hist(
            lista_x, bins=100, density=True, label="Datos Generados", edgecolor="black"
        )
        axs[0].plot(
            [a, a, b, b],
            [0, 1 / (b - a), 1 / (b - a), 0],
            label="Distribución Uniforme Teórica",
        )
        axs[0].set_title("1 repetición")
        axs[0].legend()
        print(
            f"Test Kolmogorov-Smirnov: Distribucion UniformeR entre {a=} y {b=}-> {KolmogorovTest(lista_x,0.05,'uniform',(a, b))}"
        )

axs[1].hist(total, bins=100, density=True, label="Datos Generados", edgecolor="black")
axs[1].plot(
    [a, a, b, b],
    [0, 1 / (b - a), 1 / (b - a), 0],
    label="Distribución Uniforme Teórica",
)
axs[1].set_title("x30reps")
axs[1].legend()
plt.show()

# --------------------------------EXPONENCIAL-M-RECHAZO-------------------------------------


def densidad_exponencial(x, lam):
    return lam * np.exp(-lam * x)


def exponencialR(lam, max_x, n):
    aceptados = []
    c = 1 / densidad_exponencial(0, lam)
    while len(aceptados) < n:
        # Generar número aleatorio r2
        r1 = np.random.uniform(0, 1)
        r2 = np.random.uniform(0, 1)

        # Calcular el valor de x
        x = max_x * r1
        # print(f'{x=} - {densidad_exponencial(x, lam)} - {c*densidad_exponencial(x, lam)} - {r2=}')

        # Rechazar o aceptar el valor generado según r2 y la función de densidad de probabilidad
        if r2 <= c * densidad_exponencial(x, lam):
            aceptados.append(x)

    return aceptados


lmbda = 0.5
max_x = 10
n = 10000
total = []
fig, axs = plt.subplots(ncols=2, nrows=1, constrained_layout=True, figsize=[7.5, 4])
for rep in range(30):
    lista_x = exponencialR(lmbda, max_x, n)
    total.extend(lista_x)
    if rep == 1:
        axs[0].hist(
            lista_x, bins=100, density=True, label="Datos Generados", edgecolor="black"
        )
        x = np.linspace(0, max_x, n)
        y = densidad_exponencial(x, lmbda)
        axs[0].plot(x, y, label=f"Exponencial (lambda={lmbda})")
        axs[0].set_title("1 repetición")
        axs[0].legend()
        print(
            f"Test Kolmogorov-Smirnov: Distribucion ExponencialR con λ={lmbda}-> {KolmogorovTest(lista_x,0.05,'expon',(0, 1/lmbda))}"
        )


axs[1].hist(total, bins=100, density=True, label="Datos Generados", edgecolor="black")
x = np.linspace(0, max_x, n)
y = densidad_exponencial(x, lmbda)
axs[1].plot(x, y, label=f"Exponencial (lambda={lmbda})")
axs[1].set_title("x30reps")
axs[1].legend()
plt.show()

# --------------------------------GAMMA-M-RECHAZO-------------------------------------


def densidad_gamma(x, k, alp):
    numerador = (alp**k) * (x ** (k - 1)) * exp(-alp * x)
    denominador = gamma(k)
    return numerador / denominador


def gammaR(n, k, alp, max_x):
    aceptados = []
    c = 1 / densidad_gamma(alp * (k - 1), k, alp)  # Constante de cota superior
    while len(aceptados) < n:
        r1 = np.random.uniform(
            0, 1
        )  # Generar número aleatorio a partir de la distribución exponencial
        r2 = np.random.uniform(0, 1)  # Generar número aleatorio uniforme entre 0 y 1

        x = max_x * r1

        if r2 <= c * densidad_gamma(x, k, alp):
            aceptados.append(x)

    return aceptados


lmbda = 1
k = 5
max_x = 15
n = 10000
total = []
fig, axs = plt.subplots(ncols=2, nrows=1, constrained_layout=True, figsize=[7.5, 4])
for i in range(30):
    lista_x = gammaR(n, k, lmbda, max_x)
    total.extend(lista_x)
    if i == 1:
        axs[0].hist(
            lista_x, bins=100, density=True, label="Datos Generados", edgecolor="black"
        )
        x = np.linspace(0, max_x, n)
        y = (1 / (lmbda**k * np.math.gamma(k))) * x ** (k - 1) * np.exp(-x / lmbda)
        axs[0].plot(x, y, label=f"Gamma")
        axs[0].set_title("1 repetición")
        axs[0].legend()
        print(
            f"Test Kolmogorov-Smirnov: Distribucion GammaR {lmbda=}, {k=} -> {KolmogorovTest(lista_x,0.05,'gam',(k, 0, lmbda))}"
        )


axs[1].hist(total, bins=100, density=True, label="Datos Generados", edgecolor="black")
x = np.linspace(0, max_x, n)
y = (1 / (lmbda**k * np.math.gamma(k))) * x ** (k - 1) * np.exp(-x / lmbda)
axs[1].plot(x, y, label=f"Gamma")
axs[1].set_title("x30reps")
axs[1].legend()
plt.show()

# --------------------------------NORMAL-M-RECHAZO-------------------------------------


def densidad_normal(x, m, d):
    return exp(-(((x - m) ** 2) / (2 * (d**2)))) / d * sqrt(2 * pi)


def normalR(n, m, d, factor):
    aceptados = []
    c = 1 / densidad_normal(m, m, d)  # Constante de cota superior
    while len(aceptados) < n:
        r1 = np.random.uniform(
            0, 1
        )  # Generar número aleatorio a partir de la distribución exponencial
        r2 = np.random.uniform(0, 1)  # Generar número aleatorio uniforme entre 0 y 1
        a = m - factor * d
        b = m + factor * d
        x = a + (b - a) * r1
        if r2 <= c * densidad_normal(x, m, d):
            aceptados.append(x)

    return aceptados


mu = 1
desvio = 0.5
factor = 3.5
n = 10000
total = []
fig, axs = plt.subplots(ncols=2, nrows=1, constrained_layout=True, figsize=[7.5, 4])
for i in range(30):
    lista_x = normalR(n, mu, desvio, factor)
    total.extend(lista_x)
    if i == 1:
        axs[0].hist(
            lista_x, bins=100, density=True, label="Datos Generados", edgecolor="black"
        )
        x = np.linspace(mu - factor * desvio, mu + factor * desvio, n)
        pdf = norm.pdf(x, loc=mu, scale=desvio)
        # Graficar la distribución normal teórica
        axs[0].plot(x, pdf, "r-", lw=2, label=f"Normal μ={mu} σ={desvio}")
        axs[0].set_title("1 repetición")
        axs[0].legend()
        print(
            f"Test Kolmogorov-Smirnov: Distribucion NormalR {mu=} y {desvio=}-> {KolmogorovTest(lista_x,0.05,'norm',(mu, desvio))}"
        )


axs[1].hist(total, bins=100, density=True, label="Datos Generados", edgecolor="black")
x = np.linspace(mu - factor * desvio, mu + factor * desvio, n)
pdf = norm.pdf(x, loc=mu, scale=desvio)
# Graficar la distribución normal teórica
axs[1].plot(x, pdf, "r-", lw=2, label=f"Normal μ={mu} σ={desvio}")
axs[1].set_title("x30reps")
axs[1].legend()
plt.show()

# --------------------------------PASCAL-M-RECHAZO-------------------------------------


def densidad_Pascal(k, p, x):
    a = factorial(x + k - 1) / (factorial(x) * (factorial(k - 1)))
    b = p**k
    c = (1 - p) ** (x)
    return a * b * c


def pascalR(n, k, p):
    aceptados = []
    c = 1 / densidad_Pascal(
        k, p, int(np.floor((k - 1) * (1 - p) / p))
    )  # Constante de cota superior
    while len(aceptados) < n:
        r1 = np.random.uniform(
            0, 1
        )  # Generar número aleatorio a partir de la distribución exponencial
        r2 = np.random.uniform(0, 1)  # Generar número aleatorio uniforme entre 0 y 1
        x = trunc(2 * k * r1)
        if r2 <= c * densidad_Pascal(k, p, x):
            aceptados.append(x)

    return aceptados


k = 20
p = 0.5
n = 10000
total = []
fig, axs = plt.subplots(ncols=2, nrows=1, constrained_layout=True, figsize=[7.5, 4])
for i in range(30):
    lista_x = pascalR(n, k, p)
    total.extend(lista_x)
    if i == 1:
        # graficar pascal teorica
        x = np.arange(0, np.max(lista_x) + 1)
        y = nbinom.pmf(x, k, p)
        axs[0].plot(x, y, "ro", markersize=5, label="Pascal")
        # graficar mis variables generadas
        axs[0].hist(
            lista_x,
            bins=x,
            density=True,
            label="Datos Generados",
            edgecolor="black",
            width=0.8,
        )
        axs[0].set_title("1 repetición - k=20 p=0.5")
        axs[0].legend()
        print(
            f"Test Kolmogorov-Smirnov: Distribucion PascalR {k=} y {p=}-> {KolmogorovTest(lista_x,0.05,'nbinom', (k, p))}"
        )

# graficar pascal teorica
x = np.arange(0, np.max(lista_x) + 1)
y = nbinom.pmf(x, k, p)
axs[1].plot(x, y, "ro", markersize=5, label="Pascal")
# graficar mis variables generadas
axs[1].hist(
    total, bins=x, density=True, label="Datos Generados", edgecolor="black", width=0.8
)
axs[1].set_title("x30reps - k=20 p=0.5")
axs[1].legend()
plt.show()

# --------------------------------BINOMIAL-M-RECHAZO-------------------------------------


def densidad_Binomial(n, p, x):
    a = factorial(n) / (factorial(x) * factorial(n - x))
    b = p**x
    c = (1 - p) ** (n - x)
    return a * b * c


def binomialR(cant, n, p):
    aceptados = []
    c = 1 / densidad_Binomial(n, p, round(n * p))  # Constante de cota superior
    while len(aceptados) < cant:
        r1 = np.random.uniform(
            0, 1
        )  # Generar número aleatorio a partir de la distribución exponencial
        r2 = np.random.uniform(0, 1)  # Generar número aleatorio uniforme entre 0 y 1
        x = trunc(n * r1)
        if r2 <= c * densidad_Binomial(n, p, x):
            aceptados.append(x)

    return aceptados


n = 30
p = 0.7
cant = 10000
total = []
fig, axs = plt.subplots(ncols=2, nrows=1, constrained_layout=True, figsize=[7.5, 4])
for i in range(30):
    lista_x = binomialR(cant, n, p)
    total.extend(lista_x)
    if i == 1:
        # graficar binomial teorica
        x = np.arange(0, np.max(lista_x) + 1)
        y = binom.pmf(x, n, p)
        axs[0].plot(x, y, "ro", markersize=5, label="Binomial")
        # graficar mis variables generadas
        axs[0].hist(
            lista_x,
            bins=x,
            density=True,
            label="Datos Generados",
            edgecolor="black",
            width=0.4,
        )
        axs[0].set_title("1 repetición - n=30 p=0.7")
        axs[0].legend()
        test_prob_param(lista_x, n, p)
# graficar binomial teorica
x = np.arange(0, np.max(lista_x) + 1)
y = binom.pmf(x, n, p)
axs[1].plot(x, y, "ro", markersize=5, label="Binomial")
# graficar mis variables generadas
axs[1].hist(
    total, bins=x, density=True, label="Datos Generados", edgecolor="black", width=0.4
)
axs[1].set_title("x30reps - n=30 p=0.7")
axs[1].legend()
# title('Histograma de una VA con distribucion Binomial-Metodo de Rechazo')
plt.show()

# --------------------------------HIPERGEOMETRICA-M-RECHAZO-------------------------------------


def densidad_Hipergeometrica(N, n, p, x):
    a = comb(round(N * p), x)
    b = comb(round(N * (1 - p)), n - x)
    c = comb(N, n)
    return (a * b) / c


def hipergeometricaR(cant, N, n, p):
    aceptados = []
    c = 1 / densidad_Hipergeometrica(
        N, n, p, round(n * p)
    )  # Constante de cota superior
    while len(aceptados) < cant:
        r1 = np.random.uniform(
            0, 1
        )  # Generar número aleatorio a partir de la distribución exponencial
        r2 = np.random.uniform(0, 1)  # Generar número aleatorio uniforme entre 0 y 1
        x = trunc(n * r1)
        if r2 <= c * densidad_Hipergeometrica(N, n, p, x):
            aceptados.append(x)

    return aceptados


N = 530
n = 20
p = 0.4
cant = 10000
total = []
fig, axs = plt.subplots(ncols=2, nrows=2, constrained_layout=True, figsize=[7.5, 7.5])
axs = axs.flatten()
for i in range(30):
    lista_x = hipergeometricaR(cant, N, n, p)
    total.extend(lista_x)
    if i == 1:
        # graficar hipergeometrica teorica
        x = np.arange(0, np.max(lista_x) + 1)
        y = [densidad_Hipergeometrica(N, n, p, k) for k in x]
        axs[0].plot(x, y, "ro", markersize=5, label="Hipergeometrica")
        # graficar mis variables generadas
        axs[0].hist(
            lista_x,
            bins=x,
            density=True,
            label="Datos Generados",
            edgecolor="black",
            width=0.4,
        )
        axs[0].set_title(f"1 rep - {N=} {n=} {p=}")
        axs[0].legend()
        test_qq(lista_x, N, n, p, axs, 1)
# graficar hipergeometrica teorica
x = np.arange(0, np.max(lista_x) + 1)
y = [densidad_Hipergeometrica(N, n, p, k) for k in x]
axs[2].plot(x, y, "ro", markersize=5, label="Hipergeometrica")
# graficar mis variables generadas
axs[2].hist(
    total, bins=x, density=True, label="Datos Generados", edgecolor="black", width=0.4
)
axs[2].set_title(f"x30reps - {N=} {n=} {p=}")
axs[2].legend()
test_qq(total, N, n, p, axs, 3)
# plt.title('Histograma de una VA con distribucion HiperGeo-Metodo de Rechazo x30reps')
plt.show()

# --------------------------------POISSON-M-RECHAZO-------------------------------------


def densidad_Poisson(lam, x):
    a = exp(-lam)
    b = lam**x / factorial(x)
    return a * b


def poissonR(cant, lam):
    aceptados = []
    c = 1 / densidad_Poisson(lam, lam)  # Constante de cota superior
    max_x = 2 * lam + 2 * sqrt(lam)  # aproximo el maximo valor de x significativo
    while len(aceptados) < cant:
        r1 = np.random.uniform(
            0, 1
        )  # Generar número aleatorio a partir de la distribución exponencial
        r2 = np.random.uniform(0, 1)  # Generar número aleatorio uniforme entre 0 y 1
        x = trunc(max_x * r1)
        if r2 <= c * densidad_Poisson(lam, x):
            aceptados.append(x)

    return aceptados


lmbda = 4
cant = 10000
total = []
fig, axs = plt.subplots(ncols=2, nrows=1, constrained_layout=True, figsize=[7.5, 4])
for i in range(30):
    lista_x = poissonR(cant, lmbda)
    total.extend(lista_x)
    if i == 1:
        # graficar poisson teorica
        x = np.arange(0, np.max(lista_x) + 1)
        y = poisson.pmf(x, lmbda)
        axs[0].plot(x, y, "ro", markersize=5, label=f"Poisson λ={lmbda}")
        # graficar mis variables generadas
        axs[0].hist(
            lista_x,
            bins=x,
            density=True,
            label="Datos Generados",
            edgecolor="black",
            width=0.4,
        )
        axs[0].set_title("1 repetición")
        axs[0].legend()
        print(
            f"Test Kolmogorov-Smirnov: Distribucion PoissonR λ={lmbda} -> {KolmogorovTest(lista_x,0.05,'poisson', (0,lmbda))}"
        )
# graficar poisson teorica
x = np.arange(0, np.max(total) + 1)
y = poisson.pmf(x, lmbda)
axs[1].plot(x, y, "ro", markersize=5, label=f"Poisson λ={lmbda}")
# graficar mis variables generadas
axs[1].hist(
    total, bins=x, density=True, label="Datos Generados", edgecolor="black", width=0.4
)
axs[1].set_title("x30reps")
axs[1].legend()
# Histograma de una VA con distribucion Poisson-Metodo de Rechazo
plt.show()

# --------------------------------EMPIRICA-M-RECHAZO-------------------------------------


def empiricaR(min_x, lista_fr):
    """
    min_x:valor minimo que asumira la VA que sigue la distribucion empirica
    lista_fr:frecuencia relativa de cada numero consecutivo a partir de min_x
    :!!! sum(lista_fr)==1 !!!"""
    aceptados = []
    n = len(lista_fr)
    a, b = min_x, min_x + n - 1  # minimo y maximo valor de x
    c = 1 / max(lista_fr)  # Constante de cota superior
    while len(aceptados) < cant:
        r1 = np.random.uniform(
            0, 1
        )  # Generar número aleatorio a partir de la distribución exponencial
        r2 = np.random.uniform(0, 1)  # Generar número aleatorio uniforme entre 0 y 1
        x = round((b - (a - 0.5)) * r1)
        if x > b - a:
            continue
        elif r2 <= c * lista_fr[x]:
            aceptados.append(x)

    return aceptados


fr_empirica = [0.01, 0.09, 0.03, 0.06, 0.04, 0.07, 0.1, 0.3, 0.3]
min_x = 2
cant = 10000
total = []
fig, axs = plt.subplots(ncols=2, nrows=1, constrained_layout=True, figsize=[7.5, 4])
for i in range(30):
    lista_x = empiricaR(min_x, fr_empirica)
    total.extend(lista_x)
    if i == 1:
        # graficar empirica teorica
        x = list(range(min_x, len(fr_empirica) + min_x))
        axs[0].plot(x, fr_empirica, "ro", markersize=5, label="Empirica")
        # graficar mis variables generadas
        axs[0].bar(
            x,
            np.bincount(lista_x) / len(lista_x),
            align="center",
            label="Datos Generados",
        )
        print(np.bincount(lista_x) / len(lista_x))
        # plt.hist(lista_x, bins=len(fr_empirica), align='mid',width=0.4, weights=[1/cant]*cant,label='Datos Generados',edgecolor='black')
        axs[0].set_title("1 repeticion")
        axs[0].legend()

# graficar Empirica teorica
x = list(range(min_x, len(fr_empirica) + min_x))
axs[1].plot(x, fr_empirica, "ro", markersize=5, label="Empirica")
# graficar mis variables generadas
axs[1].bar(x, np.bincount(total) / len(total), align="center", label="Datos Generados")
print(np.bincount(total) / len(total))
axs[1].set_title("x30reps")
axs[1].legend()
# plt.title('Histograma de una VA con distribucion Empirica-Metodo de Rechazo')
plt.show()
