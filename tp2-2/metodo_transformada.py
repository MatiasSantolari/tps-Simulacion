from math import sqrt, log
from matplotlib import pyplot as plt
import numpy as np
from scipy.special import erfinv
import random
from scipy.stats import norm
from metodo_rechazo import KolmogorovTest, densidad_exponencial


def ExponencialT(pseudo: list, lmbda: float) -> list:
    expo = []
    for r in pseudo:
        x = log(1 - r) / (-lmbda)
        expo.append(x)
    return expo


def UniformeT(pseudo: list, a: float, b: float) -> list:
    """pseudo: Lista de numeros pseudoaleatorios
    a:valor minimo
    b:valor maximo
    returns: Lista distribuida uniformemente en [a,b]"""
    # la func de densidad es 1/b-a
    # la func de acumulacion es x-a/b-a
    uni = []
    for r in pseudo:
        x = a + (b - a) * r
        uni.append(x)
    return uni


def NormalT(pseudo: list, mu: float, sigma: float) -> list:
    norm = []
    for r in pseudo:
        x = mu + (sqrt(2) * sigma * erfinv((2 * r) - 1))
        norm.append(x)
    return norm


# ----------------------------------UNIFORME-M-TRANSFORMADA-------------------------------------
a, b = 5, 20
total = []
fig, axs = plt.subplots(ncols=2, nrows=1, constrained_layout=True, figsize=[7.5, 4])
for rep in range(30):
    dist = [random.random() for _ in range(10000)]
    dist = UniformeT(dist, a, b)
    total.extend(dist)
    if rep == 1:
        axs[0].hist(
            dist, bins=100, density=True, label="Datos Generados", edgecolor="black"
        )
        axs[0].plot(
            [a, a, b, b],
            [0, 1 / (b - a), 1 / (b - a), 0],
            label="Distribución Uniforme Teórica",
        )
        axs[0].set_title("1 repetición")
        axs[0].legend()
        print(
            f"Test Kolmogorov-Smirnov: Distribucion UniformeT entre {a=} y {b=}-> {KolmogorovTest(dist,0.05,'uniform',(a, b))}"
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


# ----------------------------------NORMAL-M-TRANSFORMADA-------------------------------------
mu, desvio = 1, 0.5
factor = 3.5
n = 10000
total = []
fig, axs = plt.subplots(ncols=2, nrows=1, constrained_layout=True, figsize=[7.5, 4])
for rep in range(30):
    dist = [random.random() for _ in range(10000)]
    dist = NormalT(dist, mu, desvio)
    total.extend(dist)
    if rep == 1:
        axs[0].hist(
            dist, bins=100, density=True, label="Datos Generados", edgecolor="black"
        )
        x = np.linspace(mu - factor * desvio, mu + factor * desvio, n)
        pdf = norm.pdf(x, loc=mu, scale=desvio)
        # Graficar la distribución normal teórica
        axs[0].plot(x, pdf, "r-", lw=2, label=f"Normal μ={mu} σ={desvio}")
        axs[0].set_title("1 repetición")
        axs[0].legend()
        print(
            f"Test Kolmogorov-Smirnov: Distribucion NormalT  μ={mu} σ={desvio}-> {KolmogorovTest(dist,0.05,'norm',(mu, desvio))}"
        )

axs[1].hist(total, bins=100, density=True, label="Datos Generados", edgecolor="black")
x = np.linspace(mu - factor * desvio, mu + factor * desvio, n)
pdf = norm.pdf(x, loc=mu, scale=desvio)
# Graficar la distribución normal teórica
axs[1].plot(x, pdf, "r-", lw=2, label=f"Normal μ={mu} σ={desvio}")
axs[1].set_title("x30reps")
axs[1].legend()
plt.show()


# ----------------------------------EXPONENCIAL-M-TRANSFORMADA-------------------------------------
lmbda = 0.5
max_x = 10
n = 10000
total = []
fig, axs = plt.subplots(ncols=2, nrows=1, constrained_layout=True, figsize=[7.5, 4])
for rep in range(30):
    dist = [random.random() for _ in range(10000)]
    dist = ExponencialT(dist, lmbda)
    total.extend(dist)
    if rep == 1:
        axs[0].hist(
            dist,
            bins=120,
            density=True,
            label="Datos Generados",
            edgecolor="black",
            linewidth=0.5,
        )
        x = np.linspace(0, 12, n)
        y = densidad_exponencial(x, lmbda)
        axs[0].plot(x, y, "r-", lw=1.5, label=f"Exponencial (λ={lmbda})")
        axs[0].set_title("1 repetición")
        axs[0].set_xlim(right=12)
        axs[0].legend()
        print(
            f"Test Kolmogorov-Smirnov: Distribucion ExponencialR con λ={lmbda}-> {KolmogorovTest(dist,0.05,'expon',(0, 1/lmbda))}"
        )


axs[1].hist(total, bins=130, density=True, label="Datos Generados", edgecolor="black")
x = np.linspace(0, 12, n)
y = densidad_exponencial(x, lmbda)
axs[1].plot(x, y, "r-", lw=1.5, label=f"Exponencial (λ={lmbda})")
axs[1].set_title("x30reps")
axs[1].set_xlim(right=12)
axs[1].legend()
plt.show()
