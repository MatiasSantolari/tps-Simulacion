import random
import matplotlib.pyplot as plt

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

def graf_frec_rel_labo(ppg,tipo):
  x, y = [], []
  x = sorted(list(set(ppg)))
  for valor in x:
    y.append(ppg.count(valor))
  
  #Gráfico de barras
  fig, ax = plt.subplots()
  ax.bar(x = x, height = y)
  plt.xlabel("Número de tiradas")
  plt.ylabel("Fr")
  plt.title("Frecuencia relativa de obtener apuesta favorable - LABOUCHERE - " + tipo)
  plt.show()

# LABOUCHERE CON CAPITAL FINITO
def labouchere(capital, secuencia, repeticiones):
    secuenciaAux = secuencia.copy()
    capitalAux = capital
    historial_capital = []
    total_ganadas = []
    ppg_total = []
    for i in range(repeticiones):
      capital = capitalAux
      #secuencia.clear()
      secuencia = secuenciaAux.copy()
      total_ganadas = []
      perdidas_por_ganada = [] #almacena la cantidad de tiradas que pierde antes de ganar
      tirada = 0 # contador para saber cada cuantas tiradas gana (cuantas tiradas pierde antes de ganar)
      historial = [capital]  # Guardamos el valor del capital después de cada apuesta
      while len(secuencia)  >= 2 and capital > 0:
          apuesta = secuencia[0] + secuencia[-1]  # Se calcula la próxima apuesta
          tirada += 1
          if apuesta > capital:  # Si la apuesta supera el capital disponible, se apuesta lo que queda del capital
              print(f"Perdiste {apuesta}. Capital disponible: {capital} PERDISTE LA PARTIDA")
              break
          seleccion_apuesta = random.choice(matriz_tipos_apuestas[:4])  # esto selecciona la apuesta que hará el usuario
          nroRuleta = random.randint(0, 36)  # esto selecciona el numero que saldrá en la ruleta
          if nroRuleta in seleccion_apuesta:
              resultado = 'ganar'
          else:
              resultado = 'perder'
          #resultado = random.choice(['ganar', 'perder'])  # Se simula el resultado de la apuesta
          if resultado == 'ganar':
              total_ganadas.append(1)
              perdidas_por_ganada.append(tirada) 
              tirada = 0 #reinicio el valor para saber cuantas tiradas jugará luego de ganar
              capital += apuesta
              print(f"Ganaste {apuesta}. Capital disponible: {capital}")
              historial.append(capital)  # Guardamos el valor del capital después de cada apuesta
              secuencia = secuencia[1:-1]  # Se elimina el primer y último número de la secuencia
              if len(secuencia) >= 2:
                  apuesta = secuencia[0] + secuencia[-1]  # Se calcula la próxima apuesta
              else:
                  print("La secuencia está vacía o tiene menos de 2 elementos.")
          else:
              total_ganadas.append(0)
              capital -= apuesta
              print(f"Perdiste {apuesta}. Capital disponible: {capital}")
              historial.append(capital)  # Guardamos el valor del capital después de cada apuesta
              secuencia.append(apuesta)  # Se agrega el monto de la apuesta a la secuencia
              if capital <= 0:  # Si el capital llega a cero, se pierde la partida
                  print("Te quedaste sin capital. Perdiste la partida.")
          print(secuencia)
      if len(secuencia) == 0 and capital > 0:  # Si se completó la secuencia y aún queda capital disponible, se gana la partida
          print("Completaste la secuencia. Ganaste la partida.")
      historial_capital.append(historial)
      ppg_total.extend(perdidas_por_ganada)
      # Graficamos el historial de capital
      plt.plot(historial)
      plt.xlabel('Número de tiradas')
      plt.ylabel('Capital')
      plt.title('LABOUCHERE - CAPITAL FINITO')
      plt.show()
      graf_frec_rel_labo(perdidas_por_ganada, 'capital finito')
      # # Gráfico de barras
      """
      x, y = [], []
      for i in range(len(total_ganadas)):
          x.append(i + 1)
          y.append(sum(total_ganadas[:(i + 1)]) / (i + 1))
      fig, ax = plt.subplots()
      ax.bar(x=x, height=y)
      plt.ylabel('Frecuencia relativa')
      plt.xlabel('Número de tiradas')
      plt.title('LABOUCHERE - CAPITAL FINITO')
      plt.axhline(0.48, color='g', linestyle='-', label="Frecuencia relativa esperada")
      plt.show()
      """

      capital = capitalAux
      #secuencia = secuenciaAux
      total_ganadas = []
    #graficar las 5 juntas
    for i in range(len(historial_capital)):
        plt.plot(historial_capital[i])
    plt.ylabel('Capital')
    plt.xlabel('Número de tiradas')
    plt.title('LABOUCHERE - CAPITAL FINITO')
    plt.show()
    graf_frec_rel_labo(ppg_total, 'total - Capital finito')


# Ejemplo de uso
print("<Labouchere-finito>")
capital_inicial = 300
secuencia = [10, 20, 30, 40, 50, 50, 40, 30, 20, 10]
labouchere(capital_inicial, secuencia, 5)

# LABOUCHERE CON CAPITAL INFINITO
def labouchere_infinito(secuencia, repeticiones):
    secuenciaAux = secuencia.copy()
    total_ganadas = []
    registro_historiales = []
    ppg_total=[]
    for i in range(repeticiones):
        capital = 300 # Capital inicial
        historial_capital = [capital]  # Iniciamos el historial con el capital inicial
        perdidas_por_ganada = [] #almacena la cantidad de tiradas que pierde antes de ganar
        tirada = 0 # contador para saber cada cuantas tiradas gana (cuantas tiradas pierde antes de ganar)
        secuencia = secuenciaAux.copy()
        apuesta = secuencia[0] + secuencia[-1]  # Suma el primer y último número de la secuencia para obtener la apuesta inicial
        while len(secuencia)  >= 2:
            seleccion_apuesta = random.choice(matriz_tipos_apuestas[:4])  # esto selecciona la apuesta que hará el usuario
            nroRuleta = random.randint(0, 36)  # esto selecciona el numero que saldrá en la ruleta
            tirada += 1
            if nroRuleta in seleccion_apuesta:
                resultado = 'ganar'
            else:
                resultado = 'perder'
            # resultado = random.choice(['ganar', 'perder'])  # Se simula el resultado de la apuesta
            if resultado == 'ganar':
                total_ganadas.append(1)
                perdidas_por_ganada.append(tirada) 
                tirada = 0 #reinicio el valor para saber cuantas tiradas jugará luego de ganar
                capital += apuesta
                print(f"Ganaste {apuesta}. Capital disponible: {capital}")
                historial_capital.append(capital)  # Agregamos el nuevo capital al historial
                secuencia = secuencia[1:-1]  # Se elimina el primer y último número de la secuencia
                if len(secuencia) >= 2:
                    apuesta = secuencia[0] + secuencia[-1]  # Se calcula la próxima apuesta
                else:
                    print("La secuencia está vacía o tiene menos de 2 elementos.")
            else:
                total_ganadas.append(0)
                capital -= apuesta
                print(f"Perdiste {apuesta}. Capital disponible: {capital}")
                historial_capital.append(capital)  # Agregamos el nuevo capital al historial
                secuencia.append(apuesta)  # Se agrega el monto de la apuesta a la secuencia
                if len(secuencia) >= 2:
                    apuesta = secuencia[0] + secuencia[-1]  # Se calcula la próxima apuesta
                else:
                    print("La secuencia está vacía o tiene menos de 2 elementos.")
                #if capital <= 0:  # Si el capital llega a cero, se pierde la partida
                #    print("Te quedaste sin capital. Perdiste la partida.")
                #    break
            print(secuencia)

        if len(secuencia) == 0 and capital > 0:  # Si se completó la secuencia y aún queda capital disponible, se gana la partida
            print("Completaste la secuencia. Ganaste la partida.")
        else:
            print("Perdiste")
        plt.plot(historial_capital)  # Graficamos el historial de capital
        plt.xlabel('Numero de tiradas')
        plt.ylabel('Capital')
        plt.title('LABOUCHERE - CAPITAL INFINITO')
        plt.show()
        ppg_total.extend(perdidas_por_ganada)
        registro_historiales.append(historial_capital)
        graf_frec_rel_labo(perdidas_por_ganada,'capital infinito')
        # # Gráfico de barras
        """
        x, y = [], []
        for i in range(len(total_ganadas)):
            x.append(i + 1)
            y.append(sum(total_ganadas[:(i + 1)]) / (i + 1))
        fig, ax = plt.subplots()
        ax.bar(x=x, height=y)
        plt.ylabel('Frecuencia relativa')
        plt.xlabel('Número de tiradas')
        plt.title('LABOUCHERE - CAPITAL INFINITO')
        plt.axhline(0.48, color='g', linestyle='-', label="Frecuencia relativa esperada")
        plt.show()
        total_ganadas = []"""
    # graficar las 5 juntas
    for i in range(len(registro_historiales)):
        plt.plot(registro_historiales[i])
    plt.ylabel('Capital')
    plt.xlabel('Número de tiradas')
    plt.title('LABOUCHERE - CAPITAL FINITO')
    plt.show()
    graf_frec_rel_labo(ppg_total, 'total - Capital infinito')

# Ejemplo de uso
print("<Labouchere-infinito>")
secuencia = [10, 20, 30, 40, 50, 50, 40, 30, 20, 10]
num_tiradas = 5
labouchere_infinito(secuencia, num_tiradas)
