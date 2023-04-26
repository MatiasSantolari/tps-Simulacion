import random
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------ FIBONACCI ------------------------------
def graf_historiales_fibonacci(registros, tipo):
    for i in range(len(registros)):
        plt.plot(registros[i])
    plt.ylabel('Capital')
    plt.xlabel('Número de tiradas')
    plt.title('FIBONACCI - ' + tipo)
    plt.show()

def graf_frec_rel_fibo(ppg,tipo):
  x, y = [], []
  x = sorted(list(set(ppg)))
  for valor in x:
    y.append(ppg.count(valor))
  
  #Gráfico de barras
  fig, ax = plt.subplots()
  ax.bar(x = x, height = y)
  plt.xlabel("Número de tiradas")
  plt.ylabel("Fr")
  plt.title("Frecuencia relativa de obtener apuesta favorable - FIBONACCI - " + tipo)
  plt.show()

def graficar_fibonacci(historial_capital, ppg, tipo):
    plt.plot(historial_capital)
    plt.ylabel('Capital')
    plt.xlabel('Número de tiradas')
    plt.title('FIBONACCI - ' + tipo)
    plt.show()
    # Datos
    x, y = [], []
    x = sorted(list(set(ppg)))
    for valor in x:
      y.append(ppg.count(valor))
    
    #Gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(x = x, height = y)
    plt.xlabel("Número de tiradas")
    plt.ylabel("Fr")
    plt.title("Frecuencia relativa de obtener apuesta favorable - FIBONACCI - " + tipo)
    plt.show()


def proxima_apuesta_fibonacci(resultado, apuesta_actual, apuesta_anterior, apuesta_anterior_2):
    if resultado == 'GANA':
        if apuesta_actual == 2 or apuesta_actual == 1:  # cuando gano con apuesta 2 o 1, vuelvo o mantengo los valores iniciales
            apuesta = 1
            apuesta_anterior = 0
            apuesta_anterior_2 = 0
        elif apuesta_anterior_2 != 0:
            apuesta = apuesta_anterior_2
            apuesta_anterior = apuesta_anterior - apuesta_anterior_2
            apuesta_anterior_2 = apuesta_anterior_2 - apuesta_anterior
    elif resultado == 'PIERDE':
        apuesta_anterior_2 = apuesta_anterior
        apuesta_anterior = apuesta_actual
        apuesta = apuesta_anterior + apuesta_anterior_2

    return (apuesta, apuesta_anterior, apuesta_anterior_2)


def fibonacci(capital, repeticiones):
    registro_historiales = []
    ppg_total = []
    for _ in range(repeticiones):
        capital = 100
        rondas_ganadas = 0
        rondas_total = 0
        historial_capital = []  # al finalizar cada ronda registro el capital para después graficarlo
        perdidas_por_ganada = [] #almacena la cantidad de tiradas que pierde antes de ganar
        total_ganadas = []  # para almacenar resultado de cada ronda
        tirada = 0 # contador para saber cada cuantas tiradas gana (cuantas tiradas pierde antes de ganar)
        apuesta_pre_anterior = 0
        apuesta_anterior = 0
        apuesta = 1  # Empezamos apostando 1
        while capital > 0 and capital >= apuesta:
            historial_capital.append(capital)
            rondas_total += 1
            tirada += 1
            seleccion_apuesta = random.choice(
                matriz_tipos_apuestas[:4])  # esto selecciona la apuesta que hará el usuario
            nroRuleta = random.randint(0, 36)  # esto selecciona el numero que saldrá en la ruleta
            # resultado = random.choice(['ganar', 'perder']) # Se simula el resultado de la apuesta
            if nroRuleta in seleccion_apuesta:
                rondas_ganadas += 1
                perdidas_por_ganada.append(tirada) 
                tirada = 0 #reinicio el valor para saber cuantas tiradas jugará luego de ganar
                total_ganadas.append(1)  # agrego uno si gana
                capital += apuesta
                # print(f"Ganaste {apuesta}. Capital disponible: {capital}")
                (apuesta, apuesta_anterior, apuesta_pre_anterior) = proxima_apuesta_fibonacci('GANA', apuesta,
                                                                                              apuesta_anterior,
                                                                                              apuesta_pre_anterior)
            else:
                capital -= apuesta
                total_ganadas.append(0)  # agrego cero si pierde
                # print(f"Perdiste {apuesta}. Capital disponible: {capital}")
                (apuesta, apuesta_anterior, apuesta_pre_anterior) = proxima_apuesta_fibonacci('PIERDE', apuesta,
                                                                                              apuesta_anterior,
                                                                                              apuesta_pre_anterior)
        historial_capital.append(capital)
        ppg_total.extend(perdidas_por_ganada)
        registro_historiales.append(historial_capital)
        print("RONDAS TOTALES: " + str(rondas_total))
        print("RONDAS GANADAS: " + str(rondas_ganadas))
        print("CAPITAL FINAL: " + str(capital))
        print("HISTORIAL SECUENCIA CAPITAL: " + str(historial_capital))
        graficar_fibonacci(historial_capital, perdidas_por_ganada, 'CAPITAL FINITO')
    graf_frec_rel_fibo(ppg_total, 'Capital finito')
    graf_historiales_fibonacci(registro_historiales, 'CAPITAL FINITO')


def fibonacci_infinito(tiradas, repeticiones):
    registro_historiales = []
    ppg_total = []
    for _ in range(repeticiones):
        capital = 0
        rondas_ganadas = 0
        rondas_total = 0
        perdidas_por_ganada = [] #almacena la cantidad de tiradas que pierde antes de ganar
        historial_capital = []  # al finalizar cada ronda registro el capital para después graficarlo
        total_ganadas = []  # para almacenar resultado de cada ronda
        tirada = 0 # contador para saber cada cuantas tiradas gana (cuantas tiradas pierde antes de ganar)
        apuesta_pre_anterior = 0
        apuesta_anterior = 0
        apuesta = 1  # Empezamos apostando 1
        for _ in range(tiradas):
            historial_capital.append(capital)
            rondas_total += 1
            tirada += 1
            seleccion_apuesta = random.choice(
                matriz_tipos_apuestas[:4])  # esto selecciona la apuesta que hará el usuario
            nroRuleta = random.randint(0, 36)  # esto selecciona el numero que saldrá en la ruleta
            # resultado = random.choice(['ganar', 'perder']) # Se simula el resultado de la apuesta
            if nroRuleta in seleccion_apuesta:
                rondas_ganadas += 1
                perdidas_por_ganada.append(tirada) 
                tirada = 0 #reinicio el valor para saber cuantas tiradas jugará luego de ganar
                total_ganadas.append(1)  # agrego uno si gana
                capital += apuesta
                # print(f"Ganaste {apuesta}. Capital disponible: {capital}")
                (apuesta, apuesta_anterior, apuesta_pre_anterior) = proxima_apuesta_fibonacci('GANA', apuesta,
                                                                                              apuesta_anterior,
                                                                                              apuesta_pre_anterior)
            else:
                capital -= apuesta
                total_ganadas.append(0)  # agrego cero si pierde
                # print(f"Perdiste {apuesta}. Capital disponible: {capital}")
                (apuesta, apuesta_anterior, apuesta_pre_anterior) = proxima_apuesta_fibonacci('PIERDE', apuesta,
                                                                                              apuesta_anterior,
                                                                                              apuesta_pre_anterior)
        historial_capital.append(capital)
        ppg_total.extend(perdidas_por_ganada)
        registro_historiales.append(historial_capital)
        print("RONDAS TOTALES: " + str(rondas_total))
        print("RONDAS GANADAS: " + str(rondas_ganadas))
        print("CAPITAL FINAL: " + str(capital))
        print("HISTORIAL SECUENCIA CAPITAL: " + str(historial_capital))
        graficar_fibonacci(historial_capital, perdidas_por_ganada, 'CAPITAL INFINITO')
    graf_frec_rel_fibo(ppg_total, 'capital infinito')
    graf_historiales_fibonacci(registro_historiales, 'CAPITAL INFINITO')


docena_primera = [x for x in range(1, 13)]
docena_segunda = [x for x in range(13, 25)]
docena_tercera = [x for x in range(25, 37)]
columna_primera = [x for x in range(1, 37, 3)]
columna_segunda = [x for x in range(2, 37, 3)]
columna_tercera = [x for x in range(3, 37, 3)]
numero_par = [x for x in range(1, 37) if x % 2 == 0]
numero_impar = [x for x in range(1, 37) if x % 2 != 0]
numero_rojo = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
numero_negro = (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)
claves_apuestas = ['P', 'I', 'R', 'N', 'D1', 'D2', 'D3', 'C1', 'C2', 'C3']
matriz_tipos_apuestas = [numero_par, numero_impar, numero_rojo, numero_negro, docena_primera, docena_segunda,
                         docena_tercera, columna_primera, columna_segunda, columna_tercera]

tabla_pago = {'C1': 2, 'C2': 2, 'C3': 2, 'D1': 2, 'D2': 2, 'D3': 2, 'P': 1, 'I': 1, 'N': 1, 'R': 1,
              '0': 35, '1': 35, '2': 35, '3': 35, '4': 35, '5': 35, '6': 35, '7': 35, '8': 35, '9': 35,
              '10': 35, '11': 35, '12': 35, '13': 35, '14': 35, '15': 35, '16': 35, '17': 35, '18': 35,
              '19': 35, '20': 35, '21': 35, '22': 35, '23': 35, '24': 35, '25': 35, '26': 35, '27': 35,
              '28': 35, '29': 35, '30': 35, '31': 35, '32': 35, '33': 35, '34': 35, '35': 35, '36': 35,
              }

# Ejemplo de uso de FIBONACCI CON CAPITAL FINITO
print("<Fibonacci-finito>")
capital = 100
reps = 5
fibonacci(capital,reps)

#Ejemplo FIBONACCI CON CAPITAL INFINITO
print("<Fibonacci-infinito>")
nro_tiradas = 1000
reps = 5
fibonacci_infinito(nro_tiradas, reps)
