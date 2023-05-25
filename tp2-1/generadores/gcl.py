import numpy as np
import matplotlib.pyplot as plt

# from tests.test import testKS, testChiCuadrada, testPoker, testCorridas

# Generador Congruencial Lineal (GCL)
# Forma --> Xsub(n+1) = (a Xsub(n) + c) mod (m)
# Están determinados por los parámetros: * Módulo:  m > 0
# Multiplicador 0 <= a <= m
# Incremento c <= m
# Semilla 0 <= X sub0 <= m


def generate_gcl(seed, a, c, m, n):
    numbers = []
    next = seed
    for i in range(n):
        next = ((a * next) + c) % m
        numbers.append(next / m)
    return numbers


seeds = [1234321, 2500, 6512, 6565]  # lista de Semillas
a = 22695477  # multiplicador
c = 1  # incrementador
m = 2**32  # modulo
n = 10000  # numeros pseudoaleatorios

pseudos = []
for x in seeds:
    # distribucion uniforme (0,1)
    pseudos.append(generate_gcl(x, a, c, m, n))
    # print(pseudos)

# graficos dispersion
fig, axs = plt.subplots(ncols=2, nrows=2, constrained_layout=True, figsize=[7.5, 7])
axs[0, 0].set_title(f"GCL (Semilla " + str(seeds[0]) + ")")
axs[0, 0].set(xlabel="Iteraciones (n)", ylabel="Valor Pseudoaleatorio")
axs[0, 0].scatter(range(n), pseudos[0], c="black", s=0.5)
axs[0, 1].set_title(f"GCL (Semilla " + str(seeds[1]) + ")")
axs[0, 1].set(xlabel="Iteraciones (n)", ylabel="Valor Pseudoaleatorio")
axs[0, 1].scatter(range(n), pseudos[1], c="black", s=0.5)
axs[1, 0].set_title(f"GCL (Semilla " + str(seeds[2]) + ")")
axs[1, 0].set(xlabel="Iteraciones (n)", ylabel="Valor Pseudoaleatorio")
axs[1, 0].scatter(range(n), pseudos[2], c="black", s=0.5)
axs[1, 1].set_title(f"GCL (Semilla " + str(seeds[3]) + ")")
axs[1, 1].set(xlabel="Iteraciones (n)", ylabel="Valor Pseudoaleatorio")
axs[1, 1].scatter(range(n), pseudos[3], c="black", s=0.5)
plt.show()

# graficos hist
fig, axs = plt.subplots(ncols=2, nrows=2, constrained_layout=True, figsize=[7.5, 7.5])
axs[0, 0].set_title(f"GCL (Semilla " + str(seeds[0]) + ")")
axs[0, 0].set(xlabel="numeros", ylabel="Frecuencia Absoluta")
axs[0, 0].hist(pseudos[0], edgecolor="black")

axs[0, 1].set_title(f"GCL (Semilla " + str(seeds[1]) + ")")
axs[0, 1].set(xlabel="numeros", ylabel="Frecuencia Absoluta")
axs[0, 1].hist(pseudos[1], edgecolor="black")

axs[1, 0].set_title(f"GCL (Semilla " + str(seeds[2]) + ")")
axs[1, 0].set(xlabel="numeros", ylabel="Frecuencia Absoluta")
axs[1, 0].hist(pseudos[2], edgecolor="black")

axs[1, 1].set_title(f"GCL (Semilla " + str(seeds[3]) + ")")
axs[1, 1].set(xlabel="numeros", ylabel="Frecuencia Absoluta")
axs[1, 1].hist(pseudos[3], edgecolor="black")
plt.show()

print(
    "-----------------------------------------------------------------------------------------------------"
)
testKS(pseudos[0], 0.05)
print(
    "-----------------------------------------------------------------------------------------------------"
)
testChiCuadrada(pseudos[0], 0.05)
print(
    "-----------------------------------------------------------------------------------------------------"
)
testPoker(pseudos[0], 0.05)
print(
    "-----------------------------------------------------------------------------------------------------"
)
testCorridas(pseudos[0], 0.05)

print(
    "-----------------------------------------------------------------------------------------------------"
)
testKS(pseudos[1], 0.05)
print(
    "-----------------------------------------------------------------------------------------------------"
)
testChiCuadrada(pseudos[1], 0.05)
print(
    "-----------------------------------------------------------------------------------------------------"
)
testPoker(pseudos[1], 0.05)
print(
    "-----------------------------------------------------------------------------------------------------"
)
testCorridas(pseudos[1], 0.05)

print(
    "-----------------------------------------------------------------------------------------------------"
)
testKS(pseudos[2], 0.05)
print(
    "-----------------------------------------------------------------------------------------------------"
)
testChiCuadrada(pseudos[2], 0.05)
print(
    "-----------------------------------------------------------------------------------------------------"
)
testPoker(pseudos[2], 0.05)
print(
    "-----------------------------------------------------------------------------------------------------"
)
testCorridas(pseudos[2], 0.05)

print(
    "-----------------------------------------------------------------------------------------------------"
)
testKS(pseudos[3], 0.05)
print(
    "-----------------------------------------------------------------------------------------------------"
)
testChiCuadrada(pseudos[3], 0.05)
print(
    "-----------------------------------------------------------------------------------------------------"
)
testPoker(pseudos[3], 0.05)
print(
    "-----------------------------------------------------------------------------------------------------"
)
testCorridas(pseudos[3], 0.05)
