from sys import stdin, stdout
from heapq import heappop, heappush
from collections import deque
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
def funcion_que_indica_si_se_puede_escapar_con_una_velocidad_dada(grafo_conexiones, nodo_de_inicio_de_lion, salidas, velocidad_de_mumm_ra, velocidad_a_probar, distancias_del_enemigo_a_cada_punto):
    se_ha_logrado_un_escape = False
    if nodo_de_inicio_de_lion in salidas: se_ha_logrado_un_escape = True
    elif velocidad_a_probar > 0:
        arreglo_de_distancias_maximas_permitidas_para_recorrer = [velocidad_a_probar * distancia / velocidad_de_mumm_ra for distancia in distancias_del_enemigo_a_cada_punto]
        distancias_a_cada_punto_de_lion = [float("inf")] * len(grafo_conexiones)
        distancias_a_cada_punto_de_lion[nodo_de_inicio_de_lion] = 0
        cola_de_prioridad = [(0, nodo_de_inicio_de_lion)]
        while cola_de_prioridad and not se_ha_logrado_un_escape:
            distancia_actual, nodo_actual = heappop(cola_de_prioridad)
            if distancia_actual == distancias_a_cada_punto_de_lion[nodo_actual]:
                if nodo_actual in salidas: se_ha_logrado_un_escape = True
                if not se_ha_logrado_un_escape:
                    for nodo_vecino, distancia_del_camino in grafo_conexiones[nodo_actual]:
                        nueva_distancia_que_se_ha_calculado = distancia_actual + distancia_del_camino
                        if nueva_distancia_que_se_ha_calculado < distancias_a_cada_punto_de_lion[nodo_vecino] and nueva_distancia_que_se_ha_calculado < arreglo_de_distancias_maximas_permitidas_para_recorrer[nodo_vecino]:
                            distancias_a_cada_punto_de_lion[nodo_vecino] = nueva_distancia_que_se_ha_calculado
                            heappush(cola_de_prioridad, (nueva_distancia_que_se_ha_calculado, nodo_vecino))
    return se_ha_logrado_un_escape