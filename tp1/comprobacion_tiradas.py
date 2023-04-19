import numpy as np
import matplotlib.pyplot as plt

def generar_muestra(n):
  muestra = []
  media = []
  std = []
  for i in range(n):
    muestra.append(np.random.choice(valores, 37))
    media.append(np.mean(muestra))
    std.append(np.std(muestra))
  return media, std

valores = list(range(37))

muestras = [generar_muestra(10), generar_muestra(50), generar_muestra(100), generar_muestra(200), generar_muestra(400), generar_muestra(700), generar_muestra(1000)]

print("lista promedios: ")
for i in range(len(muestras)):
  print(muestras[i][0])
  print(np.mean(muestras[i][0]))

print("lista desvios: ")
for i in range(len(muestras)):
  print(muestras[i][1])
  print(np.mean(muestras[i][1]))

for i in range(len(muestras)):
    plt.figure()
    plt.hist(muestras[i][0])
    plt.axvline(x=18, color='r')
    plt.title('Muestra {}'.format(i+1))
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.show()