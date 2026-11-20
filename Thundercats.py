import sys;
from sys import stdin, stdout;
from heapq import heappop, heappush
def funcion_para_calcular_distancias_minimas(grafo_de_conexiones, nodo_origen):
    distancias_que_se_han_calculado = [float("inf")] * len(grafo_de_conexiones)
    distancias_que_se_han_calculado[nodo_origen] = 0
    cola_de_prioridad = [(0, nodo_origen)]
    while cola_de_prioridad:
        distancia_actual, nodo_actual = heappop(cola_de_prioridad)
        if distancia_actual == distancias_que_se_han_calculado[nodo_actual]: