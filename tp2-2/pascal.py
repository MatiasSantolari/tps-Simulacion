import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import nbinom

# Define los parámetros de la distribución Pascal
r = 3
p = 0.40

# Crea un array de valores para k
k = np.arange(nbinom.ppf(0.01, r, p), nbinom.ppf(0.99, r, p))

# Calcula los valores de la distribución Pascal para cada valor de k
probs = nbinom.pmf(k, r, p)

# Crea la figura y el eje
fig, ax = plt.subplots()

# Dibuja la línea de la distribución Pascal
ax.plot(k, probs, "bo-", ms=8)

# Agrega etiquetas de los ejes y título
ax.set_xlabel("Número de fracasos antes de obtener r éxitos")
ax.set_ylabel("Probabilidad")
ax.set_title("Distribución Pascal con r=3, p=0.40")

# Muestra el gráfico
plt.show()
