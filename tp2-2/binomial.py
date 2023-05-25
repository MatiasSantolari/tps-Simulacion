import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

# Define el parámetro p de la distribución binomial
p = 0.5

# Define los valores de n
ns = [20, 40, 60, 80, 100]

# Crea la figura y los ejes
fig, ax = plt.subplots()

# Recorre los valores de n
for n in ns:
    # Crea un array de valores para k
    k = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))

    # Calcula los valores de la distribución binomial para cada valor de k
    probs = binom.pmf(k, n, p)

    # Dibuja la distribución binomial
    ax.plot(k, probs, label=f"n={n}")

# Agrega etiquetas de los ejes y título
ax.set_xlabel("Número de éxitos")
ax.set_ylabel("Probabilidad")
ax.set_title("Distribución Binomial con p=0.5")

# Agrega leyenda
ax.legend()

# Muestra el gráfico
plt.show()
