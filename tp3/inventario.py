from random import random
from typing import Dict
from matplotlib import pyplot as plt
from tabulate import tabulate
import numpy as np
import math

def ExponencialT(pseudo: list, lmbda: float) -> list:
    expo = []
    for r in pseudo:
        x = math.log(1-r)/(-lmbda)
        expo.append(x)
    return expo

def EmpiricaR(pseudo: list, min_x: int, lista_fr: list) -> list:
    """pseudo: n pseudoaleatorio en [0,1]
    min_x:valor minimo que asumira la VA que sigue la distribucion empirica
    lista_fr:frecuencia relativa de cada numero consecutivo a partir de min_x
    :!!! sum(lista_fr)==1 !!!"""
    n = len(lista_fr)
    a, b = min_x, min_x+n
    frec_rel = dict()
    M = max(lista_fr)
    empiric = []
    for i in range(a, b):
        frec_rel.setdefault(i, lista_fr.pop(0))
    for U in pseudo:
        while True:
            V = np.random.uniform(0, 1)
            T = math.trunc(a+(b-a)*V)
            if T not in frec_rel.keys():
                break
            if(M*U <= frec_rel[T]):
                empiric.append(T)
                break
    return empiric

def UniformeT(pseudo: list, a: float, b: float) -> list:
    """pseudo: Lista de numeros pseudoaleatorios
    a:valor minimo
    b:valor maximo
    returns: Lista distribuida uniformemente en [a,b]"""
    # la func de densidad es 1/b-a
    # la func de acumulacion es x-a/b-a
    uni = []
    for r in pseudo:
        x = a+(b-a)*r
        uni.append(x)
    return uni

def generador_numpy(n):
    numbers = []
    for i in range(n):
        numbers.append(np.random.uniform(0, 1))
    return numbers

class Inventory():

    def __init__(self, S: int, s: int, inventory_0: int, backlog_0: int = 0) -> None:
        """
        s :Minimum stock acceptable policy
        S :Reposition stock policy"""
        self.min_stock = s
        self.max_reposition = S
        self.Item_montly_costs = 1
        self.bklog_costs = 5
        self.Item_Order_costs = 3
        self.time = 0
        self.inventory = inventory_0
        self.backlog = backlog_0
        self.montly_inv_check = []
        self.montly_bklog_check = []
        self.montly_order_costs = []
        # (time to next reposition, increment of inventory)
        self.Total_cost = 0

    def inventory_level(self) -> int:
        return self.inventory-self.backlog

    def Check_Inventory(self) -> None:
        """Montly check to register inventory levels
        and make orders to suppliers
        returns: Size of order to suppliers"""
        self.montly_inv_check.append(self.inventory)
        self.montly_bklog_check.append(self.backlog)
        # order to suplier
        order_cost = 0
        next_order = 0
        if self.inventory_level() < self.min_stock:
            next_order = self.max_reposition-self.inventory
            order_cost = 32 + next_order*self.Item_Order_costs  # 32 setup cost
        self.montly_order_costs.append(order_cost)
        return next_order

    def Average_holding_cost(self, m: int) -> float:
        """m :number of month to check the avg cost
        ADVICE: 1 <= m <= round(self.time)"""
        I = sum(self.montly_inv_check[0:m])/m
        return I*self.Item_montly_costs

    def Averge_bklog_cost(self, m: int) -> float:
        """m :number of month to check the avg cost
        ADVICE: 1 <= m <= round(self.time)"""
        I = sum(self.montly_bklog_check[0:m])/m
        return I*self.bklog_costs

    def Run_Program(self):
        orders_delivered = 0
        orden_costo = 0
        escasez_costo = 0
        mantenimiento_costo = 0
        total_costo = 0
        items_demand = []
        customer_orders = generador_numpy(10000)
        customer_orders = ExponencialT(customer_orders, 10)
        order_sizes = generador_numpy(10000)
        order_sizes = EmpiricaR(order_sizes, 1, [1/6, 1/3, 1/3, 1/6])
        deliver_lags = generador_numpy(10000)

        order_times = generador_numpy(120)
        order_times = UniformeT(order_times, .5, 1)

        nxt_cust_order = customer_orders.pop(0)
        nxt_check = 1  # 1 check per month
        nxt_items_order = 0
        nxt_delivery = 0

        Z = 0  # size of the order requested to supplier
        # first event is when an order arrive or the first month end
        month_items_demand = 0
        self.time += min(nxt_check, nxt_cust_order)

        while True:
            if self.time == nxt_check:  # monthly check
                Z = self.Check_Inventory()
                items_demand.append(month_items_demand)
                month_items_demand = 0
                if Z > 0:
                    nxt_items_order = self.time+order_times.pop(0)
                nxt_check += 1

            if self.time == nxt_items_order:  # resuply the stock
                self.inventory += Z
                Z = 0
                nxt_items_order = 0

            if self.time == nxt_cust_order:  # customer order items
                o_size = order_sizes.pop(0)
                month_items_demand += o_size
                if self.inventory < o_size:
                    # backlog items will be delivered the next delivery possible
                    self.backlog += o_size
                else:
                    self.inventory -= o_size
                    nxt_delivery = self.time+deliver_lags.pop(0)
                nxt_cust_order = self.time+customer_orders.pop(0)

            if self.time == nxt_delivery:  # delivery time
                orders_delivered += 1
                if self.backlog > self.inventory > 0:
                    dlv_xtras = self.backlog-self.inventory
                    self.backlog -= dlv_xtras
                    self.inventory = 0
                elif self.inventory > self.backlog > 0:
                    self.inventory -= self.backlog
                    self.backlog = 0
                nxt_delivery = 0

            if self.time >= 120.:
                break
            next_events = [x for x in [nxt_check, nxt_cust_order,
                                       nxt_delivery, nxt_items_order] if x > 0]
            self.time = min(next_events)

        # data
        holding_costs = []
        bklog_costs = []
        monthly_total = []
        inv_level = []
        for i in range(len(self.montly_inv_check)):
            holding_costs.append(self.Average_holding_cost(1+i))
            bklog_costs.append(self.Averge_bklog_cost(1+i))
            inv_level.append(
                self.montly_inv_check[i]-self.montly_bklog_check[i])
            # montly inv check es lista
            # montly order costs es la lista

        # graphics

        # nivel de inv
        plt.title("Niveles del inventario")
        plt.xlabel('Mes')
        plt.ylabel('Cantidad de items')
        plt.plot(self.montly_inv_check, label='Items en inventario')
        plt.plot(self.montly_bklog_check, label='Exceso de demanda')
        plt.plot(inv_level, label='Nivel de inventario')
        plt.legend()
        plt.show()

        # costo promedio
        plt.title("Costos promedios en el tiempo")
        plt.xlabel('Mes')
        plt.ylabel('Costo promedio en el mes')
        plt.plot(holding_costs, label='Costo promedio de mantenimiento')
        plt.plot(bklog_costs, label='Perdida promedio por exceso de demanda')
        plt.legend()
        plt.show()

        # demanda items
        plt.title("Demanda en el tiempo")
        plt.xlabel('Mes')
        plt.ylabel('Items demandados en el mes')
        plt.plot(items_demand, label='Items demandados')
        plt.plot(self.montly_inv_check, label='Items disponibles')
        plt.legend()
        plt.show()

        # costo mensual total
        plt.title("Gastos realizados")
        plt.xlabel('Mes')
        plt.ylabel('$ gastado')
        plt.plot(self.montly_order_costs, label='Gasto mensual en reposicion')
        bk_c = []
        h_c = []
        for i in range(len(self.montly_inv_check)):
            h=(self.montly_inv_check[i])*self.Item_montly_costs
            b=(self.montly_bklog_check[i])*self.bklog_costs
            c=self.montly_order_costs[i]
            bk_c.append(b)
            h_c.append(h)
            monthly_total.append((h+b+c))
        plt.plot(bk_c, label='Gasto mensual por exceso de demanda')
        plt.plot(h_c, label='Gasto mensual por mantenimiento')
        plt.plot(monthly_total, label='Total mensual')
        plt.legend()
        #ax.set_xlim(left=0, right=120)
        plt.show()
        total = sum(self.montly_order_costs) + sum(bk_c) + sum(h_c)
        orden_costo += sum(self.montly_order_costs)/sum(monthly_total)
        escasez_costo += sum(bk_c)/sum(monthly_total)
        mantenimiento_costo += sum(h_c)/sum(monthly_total)
        total_costo += sum(monthly_total)

        return (orden_costo, escasez_costo, mantenimiento_costo, total_costo)

orden_costo = 0
escasez_costo = 0
mantenimiento_costo = 0
total_costo = 0
S=int(input(f"Ingrese nivel de inventario máximo (S): "))
s=int(input(f"Ingrese nivel de inventario mínimo (s): "))
inventory_0=int(input(f"Ingrese nivel de inventario inicial: "))
a = Inventory(S, s, inventory_0)
for i in range(30):
    oc, ec, mc, tc = a.Run_Program()
    orden_costo += oc
    escasez_costo += ec
    mantenimiento_costo += mc
    total_costo += tc
leg = ["entradas","% orden","% esc","% manten.", "total"]
valores = [f"s={s}  S={S} I_0={inventory_0}",str(round(orden_costo*10/3,2))
  , str(round(escasez_costo*10/3,2)), str(round(mantenimiento_costo*10/3,2)), str(round(total_costo/30,2))]
coef = [f"s={s}  S={S} I_0={inventory_0}", str(round(orden_costo/30*(total_costo/30),2))
  , str(round(escasez_costo/30*(total_costo/30),2)),str(round(mantenimiento_costo/30*(total_costo/30),2)),str(round(total_costo/30,2))]
metr = [valores, coef]
print(tabulate(metr, headers=leg))

