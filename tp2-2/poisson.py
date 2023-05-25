import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

# Definimos el parámetro lambda para la distribución de Poisson
lmbda = 3.6

# Generamos una serie de valores x para evaluar la distribución
x = np.arange(0, 16)

# Calculamos los valores de la distribución de Poisson para cada valor de x
poisson = np.exp(-lmbda) * np.power(lmbda, x) / gamma(x + 1)

# Graficamos la distribución de Poisson
plt.plot(x, poisson, "b-", lw=2)

plt.title("Distribución de Poisson con $\lambda=3,6$")
plt.xlabel("Número de ocurrencias")
plt.ylabel("Probabilidad")
plt.show()
