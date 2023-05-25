import matplotlib.pyplot as plt
import numpy as np

# Define los parámetros de la distribución normal
mu = 0
sigma = 1

# Crea un array de valores para x
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)

# Calcula los valores de la distribución normal para cada valor de x
y = 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-((x - mu) ** 2) / (2 * sigma**2))

# Crea la figura y el eje
fig, ax = plt.subplots()

# Dibuja la línea de la distribución normal
ax.plot(x, y)

# Agrega etiquetas de los ejes y título
ax.set_xlabel("X")
ax.set_ylabel("Densidad de Probabilidad")
ax.set_title("Distribución Normal")

# Muestra el gráfico
plt.show()
