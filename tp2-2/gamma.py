import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# Definir los parámetros de la distribución gamma
alpha = 2.0
beta = 2.0

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Graficar las cuatro distribuciones teóricas
x = np.linspace(0, 15, 100)
ax.plot(x, gamma.pdf(x, alpha, scale=beta), "r-", label="Gamma (1, 1)")
ax.plot(x, gamma.pdf(x, alpha + 1, scale=beta), "g-", label="Gamma (2, 3)")
ax.plot(x, gamma.pdf(x, alpha, scale=beta / 2), "b-", label="Gamma (3, 0.5)")
ax.plot(x, gamma.pdf(x, alpha + 1, scale=beta / 2), "m-", label="Gamma (2, 1)")

# Agregar leyenda y título
ax.legend()
ax.set_title("Distribución Gamma")

# Mostrar el gráfico
plt.show()
