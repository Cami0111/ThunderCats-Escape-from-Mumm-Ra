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
            for nodo_vecino, distancia_del_camino in grafo_de_conexiones[nodo_actual]:
                nueva_distancia_calculada = distancia_actual + distancia_del_camino
                if nueva_distancia_calculada < distancias_que_se_han_calculado[nodo_vecino]:
                    distancias_que_se_han_calculado[nodo_vecino] = nueva_distancia_calculada