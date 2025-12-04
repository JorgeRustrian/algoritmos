import heapq
from graphviz import Graph
import os
def dijkstra(grafo, origen):
    

    if origen not in grafo:
        return None, "El nodo origen no existe en el grafo."

    
    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[origen] = 0

    padres = {nodo: None for nodo in grafo}

   
    pq = [(0, origen)]

    while pq:
        dist_actual, nodo_actual = heapq.heappop(pq)

      
        if dist_actual > distancias[nodo_actual]:
            continue

        
        for vecino, peso in grafo[nodo_actual].items():
            nueva_dist = dist_actual + peso

            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                padres[vecino] = nodo_actual
                heapq.heappush(pq, (nueva_dist, vecino))

    return distancias, padres


def reconstruir_camino(padres, destino):
    
    camino = []
    actual = destino

    while actual is not None:
        camino.append(actual)
        actual = padres[actual]

    camino.reverse()
    return camino





def generar_png_dijkstra(grafo, camino, nombre_archivo="dijkstra_paths.png"):
   
    carpeta_output = "./docs/evidencias"
    

    g = Graph(format="png")

  
    for nodo in grafo:
       
        if nodo in camino:
            g.node(nodo, color="red", fontcolor="red")
        else:
            g.node(nodo)

    
    for u in grafo:
        for v, peso in grafo[u].items():
          
            if u < v:
                g.edge(u, v, label=str(peso), color="black")

    
    for i in range(len(camino) - 1):
        u = camino[i]
        v = camino[i + 1]
        g.edge(u, v, color="red", penwidth="3")  

    ruta_png = os.path.join(carpeta_output, nombre_archivo)
    g.render(filename=ruta_png, cleanup=True)

    print(f">> Imagen generada: {ruta_png}")