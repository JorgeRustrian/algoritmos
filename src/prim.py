from graphviz import Graph
import os
def prim(grafo, nodo_inicio=None):

    if not grafo:
        return None, 0

  
    if nodo_inicio is None:
        nodo_inicio = list(grafo.keys())[0]

    visitados = set([nodo_inicio])
    aristas_mst = []
    costo_total = 0


    while len(visitados) < len(grafo):
        mejor_peso = float("inf")
        mejor_arista = None

        
        for u in visitados:
            for v, peso in grafo[u].items():
                if v not in visitados:
                    if peso < mejor_peso:
                        mejor_peso = peso
                        mejor_arista = (u, v, peso)

       
        if mejor_arista is None:
            return None, 0

       
        u, v, peso = mejor_arista
        visitados.add(v)
        aristas_mst.append((u, v, peso))
        costo_total += peso

    return aristas_mst, costo_total

def generar_png_prim(aristas_mst, nombre_archivo="prim_mst.png"):

  
    carpeta_output = "./docs/evidencias"
  
   
    g = Graph(format="png")

    
    for u, v, peso in aristas_mst:
        g.edge(u, v, label=str(peso))

   
    ruta_png = os.path.join(carpeta_output, nombre_archivo)
    g.render(filename=ruta_png, cleanup=True)

    print(" Imagen generada en: {ruta_png}")