# Especificacion del problema

## Entrada:
 - Un grafo no dirigido y ponderado $G = (V, E)$ que representa la red de caminos de la Tercera Tierra, donde: 
 $V$ es el conjunto de vértices o nodos (intersecciones), tal que $|V| = n$.
 $E \subseteq V \times V$ es el conjunto de aristas (caminos que conectan las intersecciones bidireccionalmente), tal que $|E| = m$.
 - Una funcion de peso $w: E \to \mathbb{R}^+$ que asigna a cada arista $e \in E$ una longitud conocida $d$.
 - Un vértice inicial $s \in V$, que denota la posicion de partida de Lion-O.
 - Un vértice inicial $r \in V$, que denota la posicion de partida de los mutantes de Mumm-Ra.
 - Un subconjunto de nodos objetivo $K \subseteq V$, con $|K| = k$, que representa las ubicaciones de las salidas del puerto espacial.
 - Una constante $v \in \mathbb{R}^+$, que indica la velocidad maxima inmutable de la nave de los mutantes.

## Salida:

Se espera obtener un valor $S \in \mathbb{R}^+ \cup \{-1\}$, el cual es función estrictamente de los datos definidos en la entrada $(G, w, s, r, K, v)$. El valor de $S$ se define formalmente a través de la siguiente expresión:

$$
S = 
\begin{cases} 
\min(v_L) & \text{si } \exists \gamma \in \Gamma(s, K) \text{ tal que } \forall p \in \gamma, \frac{dist_\gamma(s,p)}{v_L} < \frac{dist_G(r,p)}{v} \\ 
-1 & \text{si no existe tal } v_L \text{ para ninguna trayectoria } \pi 
\end{cases}
$$

**Donde se definen los siguientes términos:**

*   $v_L \in \mathbb{R}^+$ es una velocidad constante hipotética para Lion-O. La salida $S$ busca el mínimo valor posible de esta variable que satisfaga la inecuación.
*   $\Gamma(s, K)$ es el conjunto de todas las trayectorias continuas posibles en el grafo $G$ que inician en $s$ y terminan en algún vértice $k \in K$.
*   $p$ representa cualquier punto continuo (ya sea un vértice o un punto fraccionario intermedio en una arista) que pertenezca a la trayectoria elegida $\gamma$.
*   $dist_\gamma(s,p)$ es la distancia exacta recorrida desde el vértice de inicio $s$ hasta el punto $p$ a lo largo de la ruta específica $\gamma$, evaluada según la función de peso $w$.
*   $dist_G(r,p)$ es la distancia del camino más corto posible en todo el grafo $G$ desde la posición inicial de los mutantes $r$ hasta el punto $p$, evaluada según la función de peso $w$.
*   El valor $-1$ es el indicador numérico de fallo, utilizado cuando la inecuación de distancias y tiempos resulta insatisfactible para cualquier trayectoria (es decir, la captura es inminente e inevitable sin importar la velocidad $v_L$).

# Casos de Prueba:
## Caso de Prueba 1:
***Pseudografo Ralo con 2 Puertos de Salida***


