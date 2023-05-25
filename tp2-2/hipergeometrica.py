import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb


def hypergeometric_pmf(x, N, n, p):
    a = comb(round(N * p), x)
    b = comb(round(N * (1 - p)), n - x)
    c = comb(N, n)
    return (a * b) / c


# Parámetros de la distribución
N = 530
n = 20
p_values = [0.2, 0.4, 0.6]

# Valores de x para evaluar la distribución
x = np.arange(0, n + 1)

# Calcular la PMF para cada valor de x y cada valor de p
pmf_values = []
for p in p_values:
    pmf = [hypergeometric_pmf(k, N, n, p) for k in x]
    pmf_values.append(pmf)

# Graficar las distribuciones hipergeométricas
for i in range(len(p_values)):
    plt.plot(x, pmf_values[i], label=f"p={p_values[i]}")

plt.xlabel("Valores de x")
plt.ylabel("Probabilidad")
plt.title("Distribuciones Hipergeométricas")
plt.legend()
plt.show()
