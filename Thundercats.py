import sys;
from sys import stdin, stdout;
from heapq import heappop, heappush
from collections import deque;
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
                    heappush(cola_de_prioridad, (nueva_distancia_calculada, nodo_vecino))
    return distancias_que_se_han_calculado
def funcion_que_indica_si_existe_una_ruta_de_escape_posible(grafo_de_conexiones, nodo_de_inicio_de_lion, nodo_de_inicio_de_mumm_ra, salidas):
    se_encontro_una_ruta_posible = False
    if nodo_de_inicio_de_lion != nodo_de_inicio_de_mumm_ra:
        if nodo_de_inicio_de_lion in salidas: se_encontro_una_ruta_posible = True
        else:
            nodos_que_se_han_visitado = [False] * len(grafo_de_conexiones)
            nodos_que_se_han_visitado[nodo_de_inicio_de_lion] = True
            cola_de_nodos = deque([nodo_de_inicio_de_lion])
            while cola_de_nodos and not se_encontro_una_ruta_posible:
                nodo_actual = cola_de_nodos.popleft()
                for nodo_vecino, _ in grafo_de_conexiones[nodo_actual]:
                    if nodo_vecino != nodo_de_inicio_de_mumm_ra and not nodos_que_se_han_visitado[nodo_vecino]:
                        if nodo_vecino in salidas:
                            se_encontro_una_ruta_posible = True
                        nodos_que_se_han_visitado[nodo_vecino] = True
                        cola_de_nodos.append(nodo_vecino)       
    return se_encontro_una_ruta_posible