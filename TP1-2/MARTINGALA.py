import random
import matplotlib.pyplot as plt
import numpy as np

def graf_historiales_martingala(registros, tipo):
    for i in range(len(registros)):
        plt.plot(registros[i])
    plt.ylabel('Capital')
    plt.xlabel('Número de tiradas')
    plt.title('MARTINGALA - ' + tipo)
    plt.show()

def graficar_martin_gala(historial_capital, rondas_ganadas, rondas_total, tipo):
    plt.plot(historial_capital)
    plt.ylabel('Capital')
    plt.xlabel('Número de tiradas')
    plt.title('MARTINGALA - ' + tipo)
    plt.show()
    #Datos
    x, y = [], []
    for i in range(len(rondas_ganadas)):
        x.append(i + 1)
        y.append(sum(rondas_ganadas[:(i + 1)]) / (i + 1))
    # Gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(x=x, height=y)
    plt.ylabel('Frecuencia relativa')
    plt.xlabel('Número de tiradas')
    plt.title('MARTINGALA - ' + tipo)
    plt.axhline(0.48, color='g', linestyle='-', label="Frecuencia relativa esperada")
    plt.show()


def martin_gala(capital, apuesta, rondas_ganadas, rondas_total, historial_capital, nro_repeticiones):
        registro_historiales = []
        for i in range(nro_repeticiones):
            while capital >= 0 and apuesta < capital:
                historial_capital.append(capital)
                rondas_total += 1
                seleccion_apuesta = random.choice(
                    matriz_tipos_apuestas[:4])  # esto selecciona la apuesta que hará el usuario
                nroRuleta = random.randint(0, 36)  # esto selecciona el numero que saldrá en la ruleta
                if nroRuleta in seleccion_apuesta:
                    rondas_ganadas.append(1)
                    capital += apuesta * tabla_pago.get(
                        claves_apuestas[matriz_tipos_apuestas.index(seleccion_apuesta)])  # sumo ganancia al capital
                    # multiplico la apuesta por la tabla de pagos que corresponde según la apuesta que realizó
                    apuesta = 1  # como ganó, vuelvo a poner la apuesta en uno
                else:
                    rondas_ganadas.append(0)
                    capital -= apuesta  # descuento la apuesta del capital
                    apuesta = apuesta * 2  # al perder, duplico la proxima apuesta
            historial_capital.append(capital)
            print("RONDAS TOTALES: " + str(rondas_total))
            print("RONDAS GANADAS: " + str(len(rondas_ganadas)))
            #lista_rondas.append([rondas_ganadas, rondas_total - rondas_ganadas])
            print("CAPITAL FINAL: " + str(capital))
            print("HISTORIAL CAPITAL GANADO: " + str(historial_capital))
            graficar_martin_gala(historial_capital, rondas_ganadas, rondas_total, 'CAPITAL FINITO')

            registro_historiales.append(historial_capital)
            # reinicio los valores
            capital = 100
            apuesta = 1
            rondas_ganadas = []
            rondas_total = 0
            historial_capital = []
        graf_historiales_martingala(registro_historiales, 'CAPITAL FINITO')


def martin_gala_infinito(capital, apuesta, rondas_ganadas, rondas_total, nro_repeticiones, nro_tiradas):
    # reinicio los valores
    capital = 100
    apuesta = 1
    rondas_ganadas = []
    rondas_total = 0
    historial_capital = []
    registro_capital = []
    for j in range(nro_repeticiones):
        historial_capital = []
        for i in range(nro_tiradas):
            historial_capital.append(capital)
            rondas_total += 1
            seleccion_apuesta = random.choice(matriz_tipos_apuestas[:4])  # esto selecciona la apuesta que hará el usuario
            nroRuleta = random.randint(0, 36)  # esto selecciona el numero que saldrá en la ruleta
            if nroRuleta in seleccion_apuesta:
                rondas_ganadas.append(1)
                capital += apuesta * tabla_pago.get(
                    claves_apuestas[matriz_tipos_apuestas.index(seleccion_apuesta)])  # sumo ganancia al capital
                # multiplico la apuesta por la tabla de pagos que corresponde según la apuesta que realizó
                apuesta = 1  # como ganó, vuelvo a poner la apuesta en uno
            else:
                rondas_ganadas.append(0)
                capital -= apuesta  # descuento la apuesta del capital
                apuesta = apuesta * 2  # al perder, duplico la proxima apuesta
        historial_capital.append(capital)
        print("RONDAS TOTALES: " + str(rondas_total))
        print("RONDAS GANADAS: " + str(len(rondas_ganadas)))
        print("CAPITAL FINAL: " + str(capital))
        print("HISTORIAL SECUENCIA CAPITAL: " + str(historial_capital))
        registro_capital.append(historial_capital)
        graficar_martin_gala(historial_capital, rondas_ganadas, rondas_total, 'CAPITAL INFINITO')
        # reinicio los valores
        capital = 100
        apuesta = 1
        rondas_ganadas = []
        rondas_total = 0
        historial_capital = []
    graf_historiales_martingala(registro_capital, 'CAPITAL INFINITO')

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
claves_apuestas = ['P','I','R','N','D1','D2','D3','C1','C2','C3']
matriz_tipos_apuestas = [numero_par, numero_impar, numero_rojo, numero_negro, docena_primera, docena_segunda, docena_tercera, columna_primera, columna_segunda, columna_tercera]

tabla_pago = {'C1': 2, 'C2': 2, 'C3': 2, 'D1': 2, 'D2': 2, 'D3': 2, 'P': 1, 'I': 1, 'N': 1, 'R': 1,
              '0': 35, '1': 35, '2': 35, '3': 35, '4': 35, '5': 35, '6': 35, '7': 35, '8': 35, '9': 35,
              '10': 35, '11': 35, '12': 35, '13': 35, '14': 35, '15': 35, '16': 35, '17': 35, '18': 35,
              '19': 35, '20': 35, '21': 35, '22': 35, '23': 35, '24': 35, '25': 35, '26': 35, '27': 35,
              '28': 35, '29': 35, '30': 35, '31': 35, '32': 35, '33': 35, '34': 35, '35': 35, '36': 35,
              }

#referido al apostador
capital = 100
apuesta= 1 #refiere al capital apostado
rondas_ganadas = []
rondas_total = 0
historial_capital = [] #al finalizar cada ronda registro el capital para después graficarlo

#Ejemplo Martin Gala CON CAPITAL FINITO
print("<Martingala-finito>")
nro_repeticiones = 5
martin_gala(capital,apuesta,rondas_ganadas,rondas_total,historial_capital,nro_repeticiones)

#Ejemplo Martin Gala CON CAPITAL INFINITO
print("<Martingala-infinito>")
nro_tiradas = 1000
nro_repeticiones = 5
martin_gala_infinito(capital,apuesta,rondas_ganadas,rondas_total,nro_repeticiones,nro_tiradas)