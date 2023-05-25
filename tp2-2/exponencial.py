import numpy as np
import matplotlib.pyplot as plt

# Definir los valores de lambda
lambdas = [0.5, 1, 1.5]

# Definir los valores de x
x = np.linspace(0, 10, 100)

# Crear la figura
fig, ax = plt.subplots(figsize=(8, 6))

# Graficar la distribución para cada valor de lambda
for lmbda in lambdas:
    y = lmbda * np.exp(-lmbda * x)
    ax.plot(x, y, label=f'$\lambda$={lmbda}')

# Agregar etiquetas y leyenda
ax.set_title('Distribución exponencial')
ax.set_xlabel('Valores de x')
ax.set_ylabel('Densidad')
ax.legend()

# Mostrar la figura
plt.show()
